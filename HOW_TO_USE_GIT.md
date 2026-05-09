# Cách sử dụng Git - Đơn giản

## ✅ Git đã sẵn sàng!

Repository đã được khởi tạo với 5 commits.

## 🚀 Push lên GitHub

### Bước 1: Tạo repo trên GitHub
1. Vào https://github.com/new
2. Tên: `SignS40`
3. Chọn Public hoặc Private
4. **KHÔNG** chọn "Add README" (đã có rồi)
5. Click "Create repository"

### Bước 2: Push code
```bash
# Thêm remote
git remote add origin https://github.com/YOUR_USERNAME/SignS40.git

# Push
git push -u origin master
```

Thay `YOUR_USERNAME` bằng username GitHub của bạn.

## 📝 Các lệnh Git cơ bản

```bash
# Xem trạng thái
git status

# Xem lịch sử
git log --oneline

# Thêm file mới
git add .
git commit -m "your message"

# Push lên GitHub
git push
```

## 🎯 Xong!

Sau khi push, code sẽ có trên GitHub và mọi người có thể tải về.
