# 🔧 GitHub Pages 权限设置指南

## 解决 "Permission denied" 错误的步骤

### 1. 检查仓库设置

#### 启用 GitHub Pages
1. 进入你的 GitHub 仓库页面
2. 点击 "Settings" 标签
3. 在左侧菜单中找到 "Pages"
4. 在 "Source" 部分：
   - 选择 "GitHub Actions"
   - 这样会自动使用你的工作流文件进行部署

#### 检查分支保护设置
1. 在 Settings 中点击 "Branches"
2. 检查是否有分支保护规则
3. 如果有，确保允许 GitHub Actions 推送

### 2. 检查 Actions 权限

#### 启用 Actions
1. 在 Settings 中点击 "Actions" → "General"
2. 确保 "Actions permissions" 设置为：
   - ✅ "Allow all actions and reusable workflows"
3. 在 "Workflow permissions" 部分：
   - ✅ 勾选 "Read and write permissions"
   - ✅ 勾选 "Allow GitHub Actions to create and approve pull requests"

### 3. 检查仓库权限

#### 确保仓库是公开的
- GitHub Pages 需要公开仓库
- 私有仓库需要 GitHub Pro 或更高版本

#### 检查你的账户权限
- 确保你是仓库的所有者或管理员
- 如果不是，联系仓库所有者给予权限

### 4. 重新触发部署

#### 方法一：推送新提交
```bash
# 添加一个小的更改
echo "# Updated" >> README.md
git add README.md
git commit -m "Trigger deployment"
git push
```

#### 方法二：手动触发工作流
1. 进入仓库的 "Actions" 标签
2. 点击 "Deploy to GitHub Pages" 工作流
3. 点击 "Run workflow" 按钮
4. 选择 "main" 分支
5. 点击 "Run workflow"

### 5. 检查工作流日志

如果仍然失败：
1. 进入 "Actions" 标签
2. 点击最新的工作流运行
3. 查看详细的错误日志
4. 根据错误信息调整设置

## 常见错误及解决方案

### 错误：403 Permission denied
**原因**：GitHub Actions 没有推送权限
**解决**：
- 确保在 Settings → Actions → General 中启用了写入权限
- 检查分支保护规则

### 错误：Branch not found
**原因**：gh-pages 分支不存在
**解决**：
- 工作流会自动创建分支，确保权限正确

### 错误：Workflow not found
**原因**：工作流文件路径错误
**解决**：
- 确保 `.github/workflows/deploy.yml` 文件存在
- 检查文件语法是否正确

## 验证部署

部署成功后：
1. 等待几分钟让 GitHub Pages 构建完成
2. 访问你的网站：`https://your-username.github.io/your-repo-name`
3. 检查是否正常显示

## 获取帮助

如果问题仍然存在：
1. 检查 GitHub 状态页面
2. 查看 GitHub Actions 文档
3. 在 GitHub Community 中提问
4. 联系 GitHub 支持

---

**提示**：大多数情况下，启用 Actions 的写入权限就能解决问题！ 