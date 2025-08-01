# 内容集合

这是一个动态的内容展示网页集合，采用苹果官网设计美学，支持多个文件夹分类，提供流畅的交互体验和信息层级分明的展示。

## 项目特点

- 🎨 **苹果风格设计**：采用苹果官网的设计语言，简洁现代
- 🔄 **动态内容**：自动扫描多个文件夹，无需手动维护链接
- 📁 **多文件夹支持**：支持按文件夹分类组织内容
- 📱 **响应式布局**：适配各种设备屏幕
- ⚡ **流畅交互**：悬停效果和平滑动画
- 🔍 **自动排序**：按文件名字母序自动排序
- 🌐 **GitHub Pages 部署**：支持静态网站托管

## 文件结构

```
项目根目录/
├── README.md              # 项目说明文档
├── index.html             # 主页文件（GitHub Pages）
├── index_template.html    # 主页模板文件
├── update_index.py        # 自动更新脚本
├── paper/                 # 论文 HTML 文件目录
│   ├── Asymmetry of verification and verifier's law.html
│   ├── CODEIO.html
│   ├── LLM-SRBench.html
│   └── ... (其他论文文件)
├── leetcode/              # LeetCode 题解目录
│   ├── 128. 最长连续序列.html
│   └── ... (其他题解文件)
└── ... (其他文件夹)
```

## 🚀 GitHub Pages 部署

### 方法一：自动部署（推荐）

1. **创建 GitHub 仓库**
   - 在 GitHub 上创建新仓库
   - 仓库名建议：`your-username.github.io`（个人网站）或任意名称

2. **上传项目文件**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/your-username/your-repo-name.git
   git push -u origin main
   ```

3. **启用 GitHub Pages**
   - 进入仓库设置 → Pages
   - Source 选择 "Deploy from a branch"
   - Branch 选择 "main"
   - 保存设置

4. **访问网站**
   - 个人网站：`https://your-username.github.io`
   - 项目网站：`https://your-username.github.io/your-repo-name`

### 方法二：手动部署

1. **准备文件**
   - 确保 `index.html` 在根目录
   - 所有 HTML 文件都在对应文件夹中

2. **上传到 GitHub**
   - 创建仓库并上传所有文件
   - 启用 GitHub Pages 服务

## 🔄 动态更新功能

### 添加新内容后更新主页

1. **添加新文件**
   - 将新的 HTML 文件放入对应文件夹
   - 例如：`paper/新论文.html`

2. **运行更新脚本**
   ```bash
   python update_index.py
   ```

3. **提交更改**
   ```bash
   git add .
   git commit -m "Add new content"
   git push
   ```

### 更新脚本功能

- ✅ 自动扫描所有文件夹中的 HTML 文件
- ✅ 按文件夹分组显示
- ✅ 保持苹果风格设计
- ✅ 自动生成正确的链接
- ✅ 支持中文文件名

## 本地开发

### 前置要求

- Python 3.6 或更高版本
- 确保文件夹中包含您的 HTML 文件

### 本地预览

1. **打开终端/命令提示符**
2. **导航到项目目录**
   ```bash
   cd "D:\Documents\Gemini生成的网页"
   ```
3. **直接打开 index.html**
   - 双击 `index.html` 文件
   - 或在浏览器中打开 `file:///path/to/index.html`

## 功能说明

### 多文件夹动态扫描
- 自动扫描所有文件夹中的所有 `.html` 文件
- 按文件夹分组显示内容
- 每个文件夹显示为独立的卡片区域
- 按文件名字母序排序显示
- 添加或删除文件后，刷新页面即可看到更新

### 文件夹显示名称
- `paper/` → "论文讲解"
- `leetcode/` → "LeetCode 题解"
- `RL/` → "强化学习"
- 其他文件夹 → 首字母大写的文件夹名

### 文件访问
- 主页面：直接打开 `index.html` 或 GitHub Pages URL
- 内容页面：点击卡片链接访问具体内容

## 添加新内容

### 添加新文件夹
1. 在项目根目录创建新文件夹（如 `tutorial/`）
2. 将 HTML 文件放入该文件夹
3. 运行 `python update_index.py` 更新主页
4. 提交更改到 GitHub

### 添加新文件
1. 将新的 HTML 文件放入对应文件夹
2. 运行 `python update_index.py` 更新主页
3. 提交更改到 GitHub

## 自定义配置

### 修改文件夹显示名称

编辑 `update_index.py` 中的 `folder_display_names` 字典来更改文件夹的显示名称。

### 修改设计样式
编辑 `index_template.html` 中的样式部分来调整页面设计。

## 故障排除

### 常见问题

**Q: GitHub Pages 显示 404 错误**
- 确保 `index.html` 在仓库根目录
- 检查文件名是否正确（区分大小写）

**Q: 页面样式显示异常**
- 确保所有 CSS 样式都内嵌在 HTML 中
- 检查浏览器控制台是否有错误

**Q: 更新脚本运行失败**
- 确保 Python 版本为 3.6+
- 检查文件编码是否为 UTF-8



**Q: 页面显示空白**
- 检查文件夹是否存在且包含 HTML 文件
- 确认文件扩展名为 `.html`

**Q: 文件无法访问**
- 检查文件名是否包含特殊字符
- 确保文件编码为 UTF-8

**Q: 文件夹不显示**
- 确保文件夹中包含 `.html` 文件
- 检查文件夹名称是否正确

### 错误信息

- `ModuleNotFoundError`: 确保使用 Python 3.6+
- `PermissionError`: 尝试使用管理员权限运行
- `OSError: [Errno 98] Address already in use`: 服务器会自动处理

## 技术栈

- **前端**: HTML5, CSS3, JavaScript
- **设计**: 苹果官网风格，响应式布局
- **部署**: GitHub Pages 静态托管

## 许可证

本项目仅供学习和个人使用。

## 贡献

欢迎提交 Issue 和 Pull Request 来改进项目！

---

**注意**: 
- 添加新内容后记得运行 `python update_index.py` 更新主页
- GitHub Pages 是静态托管，直接打开 `index.html` 即可预览 