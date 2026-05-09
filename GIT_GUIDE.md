# Git Guide - S40 Sign Tool

Hướng dẫn sử dụng Git cho dự án S40 Sign Tool.

## 📊 Repository Status

✅ **Git đã được khởi tạo và cấu hình đầy đủ!**

### Commits hiện tại:
```
* 1d73fd4 - ci: Add GitHub Actions workflows and project configuration
* 0c2996e - docs: Add Git configuration and documentation files  
* 5359689 - Initial commit: S40 Certificate & Signing Tool v1.1.1
```

### Files tracked: 24 files
- Source code: 2 Python files
- Scripts: 5 shell scripts, 1 batch file
- Documentation: 5 markdown files
- Configuration: 11 config files

## 🚀 Quick Start

### 1. Kiểm tra trạng thái
```bash
git status
git log --oneline --graph
```

### 2. Tạo branch mới
```bash
# Tạo branch cho feature
git checkout -b feature/ten-tinh-nang

# Tạo branch cho bugfix
git checkout -b bugfix/ten-loi
```

### 3. Commit changes
```bash
# Stage files
git add .

# Commit với message rõ ràng
git commit -m "feat: thêm tính năng X"
```

### 4. Push lên remote
```bash
# Lần đầu push branch mới
git push -u origin feature/ten-tinh-nang

# Push tiếp theo
git push
```

## 📝 Commit Message Convention

Sử dụng [Conventional Commits](https://www.conventionalcommits.org/):

### Format:
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types:
- `feat:` - Tính năng mới
- `fix:` - Sửa lỗi
- `docs:` - Cập nhật tài liệu
- `style:` - Format code (không thay đổi logic)
- `refactor:` - Refactor code
- `perf:` - Cải thiện performance
- `test:` - Thêm/sửa tests
- `build:` - Thay đổi build system
- `ci:` - Thay đổi CI/CD
- `chore:` - Các thay đổi khác

### Examples:
```bash
# Feature
git commit -m "feat: add batch signing for multiple JARs"

# Bug fix
git commit -m "fix: resolve certificate expiry check error"

# Documentation
git commit -m "docs: update README with new features"

# Refactor
git commit -m "refactor: simplify signature removal logic"
```

## 🌿 Branching Strategy

### Main branches:
- `master` / `main` - Production-ready code
- `develop` - Development branch

### Supporting branches:
- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `hotfix/*` - Urgent fixes for production
- `release/*` - Release preparation

### Workflow:
```bash
# Tạo feature branch từ develop
git checkout develop
git checkout -b feature/new-feature

# Làm việc và commit
git add .
git commit -m "feat: implement new feature"

# Push và tạo PR
git push -u origin feature/new-feature
```

## 🔄 Common Git Commands

### Xem thông tin
```bash
# Xem status
git status

# Xem history
git log --oneline --graph --all

# Xem changes
git diff

# Xem staged changes
git diff --staged
```

### Làm việc với branches
```bash
# Liệt kê branches
git branch -a

# Chuyển branch
git checkout branch-name

# Tạo và chuyển branch
git checkout -b new-branch

# Xóa branch
git branch -d branch-name
```

### Staging và Committing
```bash
# Stage specific files
git add file1.py file2.py

# Stage all changes
git add .

# Unstage files
git restore --staged file.py

# Commit
git commit -m "message"

# Amend last commit
git commit --amend
```

### Remote operations
```bash
# Xem remotes
git remote -v

# Add remote
git remote add origin https://github.com/user/repo.git

# Fetch changes
git fetch origin

# Pull changes
git pull origin master

# Push changes
git push origin master
```

## 🔧 Git Configuration

### User config (đã cấu hình)
```bash
# Xem config
git config --list

# Set user name
git config user.name "Your Name"

# Set user email
git config user.email "your.email@example.com"
```

### Line endings (đã cấu hình)
```bash
# Windows
git config core.autocrlf true

# Linux/Mac
git config core.autocrlf input
```

## 📦 .gitignore

File `.gitignore` đã được cấu hình để ignore:

- ✅ Certificates và keystores (*.jks, *.p12)
- ✅ JAR/JAD files trong apps/
- ✅ Python cache (__pycache__, *.pyc)
- ✅ Build artifacts (build/, dist/)
- ✅ IDE files (.vscode/, .idea/)
- ✅ OS files (.DS_Store, Thumbs.db)
- ✅ Config files (config.json)
- ✅ Logs (*.log)

## 🔐 Security Best Practices

### ⚠️ KHÔNG BAO GIỜ commit:
- ❌ Certificates (*.jks, *.p12, *.cer)
- ❌ Private keys
- ❌ Passwords trong code
- ❌ API keys
- ❌ Tokens
- ❌ Config files với thông tin nhạy cảm

### ✅ Nếu đã commit nhầm:
```bash
# Remove file from Git but keep locally
git rm --cached sensitive-file.txt

# Remove from history (cẩn thận!)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch sensitive-file.txt" \
  --prune-empty --tag-name-filter cat -- --all
```

## 🚀 GitHub Setup

### 1. Tạo repository trên GitHub
```bash
# Trên GitHub: New Repository
# Tên: SignS40
# Description: S40 Certificate & Signing Tool
# Public/Private: Chọn theo nhu cầu
```

### 2. Connect local repo
```bash
# Add remote
git remote add origin https://github.com/username/SignS40.git

# Push all branches
git push -u origin master

# Push tags (nếu có)
git push --tags
```

### 3. Verify
```bash
git remote -v
# origin  https://github.com/username/SignS40.git (fetch)
# origin  https://github.com/username/SignS40.git (push)
```

## 🏷️ Tagging Releases

### Tạo tag
```bash
# Lightweight tag
git tag v1.1.1

# Annotated tag (recommended)
git tag -a v1.1.1 -m "Release version 1.1.1"

# Tag specific commit
git tag -a v1.1.0 9fceb02 -m "Release version 1.1.0"
```

### Push tags
```bash
# Push single tag
git push origin v1.1.1

# Push all tags
git push --tags
```

### List tags
```bash
git tag
git tag -l "v1.*"
```

## 🔄 Syncing with Remote

### Pull latest changes
```bash
# Fetch and merge
git pull origin master

# Fetch only
git fetch origin

# Rebase instead of merge
git pull --rebase origin master
```

### Resolve conflicts
```bash
# After conflict occurs
git status

# Edit conflicted files
# Remove conflict markers (<<<<, ====, >>>>)

# Stage resolved files
git add resolved-file.py

# Continue
git rebase --continue
# or
git merge --continue
```

## 📊 Useful Git Aliases

Thêm vào `.gitconfig`:
```bash
[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    lg = log --oneline --graph --all
    last = log -1 HEAD
    unstage = restore --staged
```

Sử dụng:
```bash
git st          # git status
git co master   # git checkout master
git lg          # git log --oneline --graph --all
```

## 🎯 Next Steps

### 1. Push lên GitHub
```bash
git remote add origin https://github.com/username/SignS40.git
git push -u origin master
```

### 2. Tạo develop branch
```bash
git checkout -b develop
git push -u origin develop
```

### 3. Setup branch protection (trên GitHub)
- Settings → Branches → Add rule
- Branch name pattern: `master`
- ✅ Require pull request reviews
- ✅ Require status checks to pass

### 4. Enable GitHub Actions
- Actions tab sẽ tự động chạy workflows
- Build và test tự động khi push/PR

## 📚 Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)

## ✅ Checklist

- [x] Git repository initialized
- [x] .gitignore configured
- [x] .gitattributes configured
- [x] Initial commit created
- [x] Documentation commits added
- [x] CI/CD commits added
- [ ] Remote repository added
- [ ] Code pushed to GitHub
- [ ] Branch protection enabled
- [ ] GitHub Actions verified

---

**Happy Git-ing!** 🚀
