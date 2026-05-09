# 🚀 Push to GitHub - Quick Guide

## ✅ Trạng thái hiện tại

Repository đã sẵn sàng với:
- ✅ 4 commits
- ✅ 26 files tracked
- ✅ .gitignore configured
- ✅ CI/CD workflows ready
- ✅ Documentation complete

## 📋 Các bước Push lên GitHub

### Bước 1: Tạo Repository trên GitHub

1. Truy cập https://github.com
2. Click nút **"New"** hoặc **"+"** → **"New repository"**
3. Điền thông tin:
   - **Repository name:** `SignS40`
   - **Description:** `S40 Certificate & Signing Tool - Create certificates and sign Java apps for Nokia S40 phones`
   - **Visibility:** 
     - ✅ **Public** (nếu muốn share với mọi người)
     - ⚪ **Private** (nếu chỉ dùng riêng)
   - **KHÔNG chọn:**
     - ❌ Add a README file (đã có rồi)
     - ❌ Add .gitignore (đã có rồi)
     - ❌ Choose a license (đã có rồi)
4. Click **"Create repository"**

### Bước 2: Connect Local Repository

Sau khi tạo repo, GitHub sẽ hiển thị hướng dẫn. Sử dụng lệnh sau:

```bash
# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/SignS40.git

# Verify remote
git remote -v
```

**Thay `YOUR_USERNAME` bằng username GitHub của bạn!**

### Bước 3: Push Code

```bash
# Push master branch
git push -u origin master
```

Nếu được yêu cầu đăng nhập:
- Username: GitHub username của bạn
- Password: **Personal Access Token** (không phải password!)

### Bước 4: Tạo Personal Access Token (nếu cần)

Nếu push bị lỗi authentication:

1. Truy cập: https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Điền:
   - **Note:** `SignS40 Push Access`
   - **Expiration:** 90 days (hoặc tùy chọn)
   - **Scopes:** ✅ `repo` (full control)
4. Click **"Generate token"**
5. **Copy token ngay** (chỉ hiển thị 1 lần!)
6. Sử dụng token này thay cho password khi push

### Bước 5: Verify trên GitHub

Sau khi push thành công, kiểm tra:

1. **Code tab:** ✅ Tất cả files đã có
2. **README:** ✅ Hiển thị đẹp
3. **Actions tab:** ✅ Workflows đang chạy (hoặc đã pass)
4. **Issues tab:** ✅ Templates có sẵn

## 🔐 Alternative: SSH Key (Recommended)

### Setup SSH Key (chỉ làm 1 lần)

```bash
# 1. Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"
# Press Enter 3 times (default location, no passphrase)

# 2. Copy public key
# Windows
type %USERPROFILE%\.ssh\id_ed25519.pub

# Linux/Mac
cat ~/.ssh/id_ed25519.pub

# 3. Add to GitHub
# - Go to: https://github.com/settings/keys
# - Click "New SSH key"
# - Title: "My Computer"
# - Paste key
# - Click "Add SSH key"

# 4. Test connection
ssh -T git@github.com
```

### Push với SSH

```bash
# Add remote với SSH URL
git remote add origin git@github.com:YOUR_USERNAME/SignS40.git

# Push
git push -u origin master
```

## 📝 Commands Summary

```bash
# Check current status
git status
git log --oneline --graph

# Add remote (HTTPS)
git remote add origin https://github.com/YOUR_USERNAME/SignS40.git

# Or add remote (SSH)
git remote add origin git@github.com:YOUR_USERNAME/SignS40.git

# Verify remote
git remote -v

# Push to GitHub
git push -u origin master

# Push tags (if any)
git push --tags
```

## 🎯 After Push

### 1. Update README badges (optional)

Thêm vào đầu README.md:
```markdown
[![GitHub](https://img.shields.io/github/license/YOUR_USERNAME/SignS40)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/YOUR_USERNAME/SignS40)](https://github.com/YOUR_USERNAME/SignS40/releases)
[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/SignS40)](https://github.com/YOUR_USERNAME/SignS40/stargazers)
```

### 2. Enable GitHub Pages (optional)

Settings → Pages → Source: `master` branch → Save

### 3. Setup Branch Protection

Settings → Branches → Add rule:
- Branch name pattern: `master`
- ✅ Require pull request reviews before merging
- ✅ Require status checks to pass before merging

### 4. Create First Release

```bash
# Tag version
git tag -a v1.1.1 -m "Release v1.1.1 - Initial public release"

# Push tag
git push origin v1.1.1
```

GitHub Actions sẽ tự động:
- Build .exe file
- Create release
- Upload artifacts

## 🐛 Troubleshooting

### Error: "remote origin already exists"

```bash
# Remove existing remote
git remote remove origin

# Add again
git remote add origin https://github.com/YOUR_USERNAME/SignS40.git
```

### Error: "Authentication failed"

- Sử dụng Personal Access Token thay vì password
- Hoặc setup SSH key

### Error: "Updates were rejected"

```bash
# Pull first
git pull origin master --allow-unrelated-histories

# Then push
git push -u origin master
```

### Error: "Permission denied (publickey)"

- Check SSH key đã add vào GitHub chưa
- Test: `ssh -T git@github.com`

## ✅ Checklist

- [ ] Đã tạo repository trên GitHub
- [ ] Đã add remote origin
- [ ] Đã push code thành công
- [ ] README hiển thị đúng trên GitHub
- [ ] GitHub Actions đã chạy
- [ ] (Optional) Đã tạo release
- [ ] (Optional) Đã setup branch protection

## 🎉 Success!

Sau khi push thành công:

1. **Share link:** `https://github.com/YOUR_USERNAME/SignS40`
2. **Clone command:** `git clone https://github.com/YOUR_USERNAME/SignS40.git`
3. **Download .exe:** Releases → Latest → Download `S40SignTool.exe`

## 📞 Need Help?

- [GitHub Docs](https://docs.github.com)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Community](https://github.community)

---

**Ready to push?** 🚀

```bash
git remote add origin https://github.com/YOUR_USERNAME/SignS40.git
git push -u origin master
```

**Good luck!** 🎊
