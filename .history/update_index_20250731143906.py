#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动更新index.html文件
扫描所有文件夹中的HTML文件并生成新的index.html
"""

import os
import re
from urllib.parse import quote

def scan_folders():
    """扫描所有文件夹中的HTML文件"""
    folders = {}
    for item in os.listdir('.'):
        if os.path.isdir(item) and not item.startswith('.'):
            html_files = sorted([f for f in os.listdir(item) if f.endswith('.html')])
            if html_files:
                folders[item] = html_files
    return folders

def generate_html_content(folders):
    """生成HTML内容"""
    # 文件夹显示名称映射
    folder_display_names = {
        'paper': '论文讲解',
        'leetcode': 'LeetCode 题解',
        'RL': '强化学习',
        'src': '论文讲解'
    }
    
    html_content = '''        <div class="update-info">
            💡 提示：添加新内容后，需要更新此页面以显示最新文件
        </div>
        
'''
    
    for folder_name, files in sorted(folders.items()):
        display_name = folder_display_names.get(folder_name, folder_name.title())
        
        html_content += f'''        <!-- {display_name} -->
        <div class="folder-section">
            <h2 class="folder-title">{display_name}</h2>
            <div class="folder-info">共 {len(files)} 个文件</div>
            <div class="grid">'''
        
        for file in files:
            title = file.replace('.html', '')
            link = f'./{folder_name}/{quote(file)}'
            html_content += f'''
                <a href="{link}" class="card">
                    <div class="card-content">
                        <h2>{title}</h2>
                        <p>点击查看详细内容</p>
                    </div>
                </a>'''
        
        html_content += '''
            </div>
        </div>

'''
    
    return html_content

def update_index_html():
    """更新index.html文件"""
    # 读取原始index.html模板
    with open('index_template.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # 扫描文件夹
    folders = scan_folders()
    
    # 生成新的HTML内容
    new_content = generate_html_content(folders)
    
    # 替换模板中的内容部分
    # 使用正则表达式找到需要替换的部分
    pattern = r'(        <div class="update-info">.*?</div>\s*)(.*?)(\s*</div>\s*<script>)'
    replacement = r'\1' + new_content + r'\3'
    
    updated_html = re.sub(pattern, replacement, template, flags=re.DOTALL)
    
    # 写入新的index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)
    
    print(f"✅ 已更新 index.html")
    print(f"📁 扫描到 {len(folders)} 个文件夹:")
    for folder, files in folders.items():
        print(f"   - {folder}: {len(files)} 个文件")

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
            margin-bottom: 60px;
        }
        .folder-title {
            font-size: 2.5em;
            font-weight: 600;
            margin-bottom: 30px;
            color: #1d1d1f;
            text-transform: capitalize;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
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
        .card-content {
            padding: 20px;
        }
        .card h2 {
            font-size: 1.5em;
            font-weight: 600;
            margin: 0 0 10px;
        }
        .card p {
            font-size: 1em;
            color: #6e6e73;
        }
        .folder-info {
            font-size: 1.1em;
            color: #86868b;
            margin-bottom: 20px;
        }
        .update-info {
            text-align: center;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 12px;
            margin-bottom: 30px;
            font-size: 0.9em;
            color: #86868b;
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