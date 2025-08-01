#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动更新index.html文件
扫描所有文件夹中的HTML文件并生成新的index.html
支持子文件夹层级结构
"""

import os
import re
from urllib.parse import quote

def scan_folders_recursive():
    """递归扫描所有文件夹中的HTML文件，支持子文件夹"""
    def scan_directory(path, depth=0):
        """递归扫描目录"""
        result = {}
        try:
            items = os.listdir(path)
            for item in sorted(items):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path) and not item.startswith('.'):
                    # 递归扫描子目录
                    sub_result = scan_directory(item_path, depth + 1)
                    if sub_result:  # 只添加有内容的子目录
                        result[item] = sub_result
                elif item.endswith('.html'):
                    # 如果是HTML文件，直接添加到当前层级
                    if depth == 0:  # 根目录下的HTML文件
                        if '__root_files__' not in result:
                            result['__root_files__'] = []
                        result['__root_files__'].append(item)
                    else:
                        # 子目录中的HTML文件
                        if '__files__' not in result:
                            result['__files__'] = []
                        result['__files__'].append(item)
        except (PermissionError, OSError):
            pass
        return result
    
    return scan_directory('.')

def count_total_files(folder_structure):
    """统计总文件数"""
    count = 0
    for key, value in folder_structure.items():
        if key == '__files__':
            count += len(value)
        elif key == '__root_files__':
            count += len(value)
        elif isinstance(value, dict):
            count += count_total_files(value)
    return count

def generate_html_content_recursive(folder_structure, current_path='', depth=0):
    """递归生成HTML内容，支持层级结构"""
    # 文件夹显示名称映射
    folder_display_names = {
        'paper': '论文讲解',
        'leetcode': 'LeetCode 题解',
        'RL': '强化学习',
        'src': '论文讲解'
    }
    
    html_content = ''
    
    # 处理当前层级的文件
    if '__files__' in folder_structure:
        files = sorted(folder_structure['__files__'])
        if files:
            html_content += f'''
        <div class="sub-folder-section" style="margin-left: {depth * 40}px;">
            <div class="sub-folder-header">
                <span class="folder-icon">📄</span>
                <span class="sub-folder-title">文件</span>
                <span class="file-count">({len(files)} 个)</span>
            </div>
            <div class="sub-grid">'''
            
            for file in files:
                title = file.replace('.html', '')
                link = f'./{current_path}/{quote(file, safe="")}' if current_path else f'./{quote(file, safe="")}'
                html_content += f'''
                <a href="{link}" class="sub-card">
                    <div class="sub-card-content">
                        <div class="card-icon">📄</div>
                        <h3>{title}</h3>
                        <p>点击查看详细内容</p>
                    </div>
                </a>'''
            
            html_content += '''
            </div>
        </div>'''
    
    # 处理子文件夹
    for folder_name, sub_structure in folder_structure.items():
        if folder_name not in ['__files__', '__root_files__']:
            display_name = folder_display_names.get(folder_name, folder_name.title())
            total_files = count_total_files(sub_structure)
            
            # 构建当前路径
            new_path = f'{current_path}/{folder_name}' if current_path else folder_name
            
            html_content += f'''
        <div class="folder-section" style="margin-left: {depth * 40}px;">
            <div class="folder-header">
                <span class="folder-icon">📁</span>
                <h2 class="folder-title">{display_name}</h2>
                <span class="file-count">({total_files} 个文件)</span>
            </div>
            <div class="folder-info">共 {total_files} 个文件</div>'''
            
            # 递归处理子文件夹
            sub_html = generate_html_content_recursive(sub_structure, new_path, depth + 1)
            html_content += sub_html
            
            html_content += '''
        </div>'''
    
    return html_content

def generate_html_content(folders):
    """生成HTML内容"""
    html_content = '''        <div class="update-info">
            <div class="update-icon">💡</div>
            <div class="update-text">
                <strong>提示：</strong>添加新内容后，需要更新此页面以显示最新文件
            </div>
        </div>
        
'''
    
    # 使用递归扫描的结果
    html_content += generate_html_content_recursive(folders)
    
    return html_content

def update_index_html():
    """更新index.html文件"""
    # 读取原始index.html模板
    with open('index_template.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # 扫描文件夹
    folders = scan_folders_recursive()
    
    # 生成新的HTML内容
    new_content = generate_html_content(folders)
    
    # 替换模板中的内容部分
    # 使用更简单的方法：替换注释标记之间的内容
    start_marker = '        <!-- 这里的内容会被自动更新 -->'
    end_marker = '    </div>'
    
    start_pos = template.find(start_marker)
    end_pos = template.find(end_marker, start_pos)
    
    if start_pos != -1 and end_pos != -1:
        updated_html = template[:start_pos] + new_content + template[end_pos:]
    else:
        # 如果找不到标记，直接替换整个容器内容
        pattern = r'(    <div class="container">\s*)(.*?)(\s*</div>\s*<script>)'
        replacement = r'\1' + new_content + r'\3'
        updated_html = re.sub(pattern, replacement, template, flags=re.DOTALL)
    
    # 写入新的index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)
    
    print(f"✅ 已更新 index.html")
    print(f"📁 扫描到文件夹结构:")
    print_folder_structure(folders)

def print_folder_structure(structure, indent=0):
    """打印文件夹结构"""
    for key, value in structure.items():
        if key == '__files__':
            print(' ' * indent + f"📄 文件: {len(value)} 个")
        elif key == '__root_files__':
            print(' ' * indent + f"📄 根目录文件: {len(value)} 个")
        elif isinstance(value, dict):
            print(' ' * indent + f"📁 {key}: {count_total_files(value)} 个文件")
            print_folder_structure(value, indent + 2)

def create_template():
    """创建index.html模板文件"""
    template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>内容集合</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f7;
            color: #1d1d1f;
            line-height: 1.4;
        }
        header {
            background-color: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(10px);
            padding: 20px;
            text-align: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid #d2d2d7;
        }
        h1 {
            font-size: 3em;
            font-weight: 600;
            margin: 0;
        }
        .container {
            max-width: 1200px;
            margin: 40px auto;
            padding: 0 20px;
        }
        .folder-section {
            margin-bottom: 40px;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.4));
            border-radius: 16px;
            padding: 25px;
            border: 1px solid rgba(0, 122, 255, 0.1);
            box-shadow: 0 4px 20px rgba(0, 122, 255, 0.08);
            position: relative;
            overflow: hidden;
        }
        .folder-section::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 4px;
            background: linear-gradient(180deg, #007AFF, #5856D6);
        }
        .folder-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 15px;
        }
        .folder-icon {
            font-size: 1.8em;
            filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
        }
        .folder-title {
            font-size: 2.2em;
            font-weight: 600;
            margin: 0;
            color: #1d1d1f;
            text-transform: capitalize;
            flex: 1;
        }
        .file-count {
            background: linear-gradient(135deg, #007AFF, #5856D6);
            color: white;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: 500;
            box-shadow: 0 2px 8px rgba(0, 122, 255, 0.3);
        }
        .sub-folder-section {
            margin-bottom: 25px;
            background: rgba(255, 255, 255, 0.6);
            border-radius: 12px;
            padding: 20px;
            border: 1px solid rgba(52, 199, 89, 0.1);
            box-shadow: 0 2px 12px rgba(52, 199, 89, 0.06);
            position: relative;
        }
        .sub-folder-section::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 3px;
            background: linear-gradient(180deg, #34C759, #30D158);
        }
        .sub-folder-header {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 15px;
        }
        .sub-folder-title {
            font-size: 1.5em;
            font-weight: 500;
            color: #1d1d1f;
            flex: 1;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        .sub-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 15px;
        }
        .card {
            background-color: white;
            border-radius: 18px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            text-decoration: none;
            color: inherit;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
        }
        .sub-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.7));
            border-radius: 12px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
            overflow: hidden;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            text-decoration: none;
            color: inherit;
            border: 1px solid rgba(255, 255, 255, 0.2);
            position: relative;
        }
        .sub-card:hover {
            transform: translateY(-4px) scale(1.02);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
            border-color: rgba(52, 199, 89, 0.3);
        }
        .sub-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #34C759, #30D158);
            transform: scaleX(0);
            transition: transform 0.3s ease;
        }
        .sub-card:hover::before {
            transform: scaleX(1);
        }
        .card-content {
            padding: 20px;
        }
        .sub-card-content {
            padding: 18px;
            text-align: center;
        }
        .card-icon {
            font-size: 2em;
            margin-bottom: 10px;
            display: block;
            filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
        }
        .card h2 {
            font-size: 1.5em;
            font-weight: 600;
            margin: 0 0 10px;
        }
        .sub-card h3 {
            font-size: 1.1em;
            font-weight: 600;
            margin: 0 0 8px;
            color: #1d1d1f;
        }
        .card p {
            font-size: 1em;
            color: #6e6e73;
        }
        .sub-card p {
            font-size: 0.85em;
            color: #86868b;
            margin: 0;
        }
        .folder-info {
            font-size: 1em;
            color: #86868b;
            margin-bottom: 20px;
            opacity: 0.8;
        }
        .update-info {
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 20px 25px;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.7));
            border-radius: 16px;
            margin-bottom: 30px;
            font-size: 0.95em;
            color: #1d1d1f;
            border: 1px solid rgba(255, 193, 7, 0.2);
            box-shadow: 0 4px 20px rgba(255, 193, 7, 0.1);
        }
        .update-icon {
            font-size: 1.5em;
            filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
        }
        .update-text {
            flex: 1;
        }
    </style>
</head>
<body>
    <header>
        <h1>内容集合</h1>
    </header>
    <div class="container">
        <!-- 这里的内容会被自动更新 -->
    </div>

    <script>
        // 平滑滚动效果
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
    </script>
</body>
</html>'''
    
    with open('index_template.html', 'w', encoding='utf-8') as f:
        f.write(template)
    
    print("✅ 已创建 index_template.html")

if __name__ == "__main__":
    # 如果模板文件不存在，先创建它
    if not os.path.exists('index_template.html'):
        create_template()
    
    # 更新index.html
    update_index_html() 