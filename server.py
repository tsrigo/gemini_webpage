import http.server
import socketserver
import os
from urllib.parse import quote
import socket

def find_available_port(start_port=8000):
    port = start_port
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('', port))
            sock.close()
            return port
        except OSError:
            port += 1

PORT = find_available_port()

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # 扫描所有文件夹
            folders = {}
            for item in os.listdir('.'):
                if os.path.isdir(item) and not item.startswith('.'):
                    html_files = sorted([f for f in os.listdir(item) if f.endswith('.html')])
                    if html_files:  # 只包含有HTML文件的文件夹
                        folders[item] = html_files
            
            html = '''<!DOCTYPE html>
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
    </style>
</head>
<body>
    <header>
        <h1>内容集合</h1>
    </header>
    <div class="container">'''
            
            for folder_name, files in sorted(folders.items()):
                # 文件夹显示名称映射
                folder_display_names = {
                    'paper': '论文讲解',
                    'leetcode': 'LeetCode 题解',
                    'src': '论文讲解'  # 兼容旧名称
                }
                display_name = folder_display_names.get(folder_name, folder_name.title())
                
                html += f'''
        <div class="folder-section">
            <h2 class="folder-title">{display_name}</h2>
            <div class="folder-info">共 {len(files)} 个文件</div>
            <div class="grid">'''
                
                for file in files:
                    title = file.replace('.html', '')
                    link = f'/{folder_name}/' + quote(file)
                    html += f'''
                <a href="{link}" class="card">
                    <div class="card-content">
                        <h2>{title}</h2>
                        <p>点击查看详细内容</p>
                    </div>
                </a>'''
                
                html += '''
            </div>
        </div>'''
            
            html += '''
    </div>
    <script>
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
            self.wfile.write(html.encode('utf-8'))
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever() 