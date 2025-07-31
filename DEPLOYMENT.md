# 🚀 GitHub Pages 部署指南

## 快速部署步骤

### 1. 准备 GitHub 账户
- 确保你有 GitHub 账户
- 如果没有，请先注册：https://github.com

### 2. 创建新仓库
1. 登录 GitHub
2. 点击右上角 "+" → "New repository"
3. 填写仓库名称（建议：`your-username.github.io` 用于个人网站）
4. 选择 "Public"（GitHub Pages 需要公开仓库）
5. 不要勾选 "Add a README file"
6. 点击 "Create repository"

### 3. 上传项目文件

#### 方法一：使用 Git 命令行
```bash
# 在项目目录中打开终端
cd "D:\Documents\Gemini生成的网页"

# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 提交更改
git commit -m "Initial commit"

# 设置主分支名称
git branch -M main

# 添加远程仓库（替换为你的仓库地址）
git remote add origin https://github.com/your-username/your-repo-name.git

# 推送到 GitHub
git push -u origin main
```

#### 方法二：使用 GitHub Desktop
1. 下载并安装 GitHub Desktop
2. 登录你的 GitHub 账户
3. 点击 "Clone a repository from the Internet"
4. 选择你刚创建的仓库
5. 选择本地保存位置
6. 将项目文件复制到克隆的文件夹中
7. 在 GitHub Desktop 中提交并推送

#### 方法三：直接上传
1. 在 GitHub 仓库页面点击 "uploading an existing file"
2. 拖拽所有项目文件到上传区域
3. 点击 "Commit changes"

### 4. 启用 GitHub Pages

1. 进入你的仓库页面
2. 点击 "Settings" 标签
3. 在左侧菜单中找到 "Pages"
4. 在 "Source" 部分：
   - 选择 "Deploy from a branch"
   - Branch 选择 "main"
   - Folder 选择 "/ (root)"
5. 点击 "Save"

### 5. 访问你的网站

等待几分钟后，你就可以访问你的网站了：

- **个人网站**：`https://your-username.github.io`
- **项目网站**：`https://your-username.github.io/your-repo-name`

## 🔄 更新内容

### 添加新内容
1. 将新的 HTML 文件放入对应文件夹
2. 运行更新脚本：
   ```bash
   python update_index.py
   ```
3. 提交更改：
   ```bash
   git add .
   git commit -m "Add new content"
   git push
   ```

### 修改现有内容
1. 编辑对应的 HTML 文件
2. 提交更改：
   ```bash
   git add .
   git commit -m "Update content"
   git push
   ```

## 📁 文件结构说明

部署后，你的仓库应该包含以下文件：

```
your-repo/
├── index.html              # 主页文件
├── index_template.html     # 主页模板
├── update_index.py         # 更新脚本
├── server.py              # 本地开发服务器
├── README.md              # 项目说明
├── DEPLOYMENT.md          # 部署指南
├── paper/                 # 论文文件夹
│   ├── 论文1.html
│   └── 论文2.html
├── leetcode/              # LeetCode 文件夹
│   ├── 题解1.html
│   └── 题解2.html
└── RL/                    # 强化学习文件夹
    └── 内容.html
```

## ⚠️ 注意事项

### 重要提醒
- ✅ 确保 `index.html` 在仓库根目录
- ✅ 所有 HTML 文件使用 UTF-8 编码
- ✅ 文件名避免使用特殊字符
- ✅ 仓库必须是公开的（GitHub Pages 要求）

### 常见问题解决

**Q: 网站显示 404 错误**
- 检查 `index.html` 是否在根目录
- 确认 GitHub Pages 已启用
- 等待几分钟让部署完成

**Q: 页面样式显示异常**
- 确保所有 CSS 都在 HTML 文件中
- 检查浏览器控制台错误

**Q: 中文文件名显示异常**
- 确保文件使用 UTF-8 编码
- 在 `update_index.py` 中已处理 URL 编码

**Q: 更新后页面没有变化**
- 清除浏览器缓存
- 检查 GitHub Pages 部署状态
- 等待几分钟让更改生效

## 🎯 自定义设置

### 修改网站标题
编辑 `index_template.html` 中的 `<title>` 标签

### 修改文件夹显示名称
编辑 `update_index.py` 中的 `folder_display_names` 字典

### 修改页面样式
编辑 `index_template.html` 中的 `<style>` 部分

## 📞 获取帮助

如果遇到问题：
1. 检查 GitHub Pages 设置
2. 查看仓库的 Actions 标签页
3. 在 GitHub Issues 中提问
4. 参考 GitHub Pages 官方文档

---

**恭喜！** 🎉 你的网站已经成功部署到 GitHub Pages！ 