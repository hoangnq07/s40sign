# Contributing to S40 Sign Tool

Cảm ơn bạn quan tâm đến việc đóng góp cho S40 Sign Tool! 🎉

## 🚀 Cách đóng góp

### 1. Fork và Clone

```bash
# Fork repo trên GitHub
# Clone về máy
git clone https://github.com/your-username/SignS40.git
cd SignS40
```

### 2. Tạo Branch mới

```bash
# Tạo branch cho feature/bugfix
git checkout -b feature/ten-tinh-nang
# hoặc
git checkout -b bugfix/ten-loi
```

### 3. Phát triển

- Viết code rõ ràng, dễ hiểu
- Thêm comments cho code phức tạp
- Tuân thủ coding style hiện tại
- Test kỹ trước khi commit

### 4. Commit

```bash
# Stage changes
git add .

# Commit với message rõ ràng
git commit -m "feat: thêm tính năng X"
# hoặc
git commit -m "fix: sửa lỗi Y"
```

**Commit message format:**
- `feat:` - Tính năng mới
- `fix:` - Sửa lỗi
- `docs:` - Cập nhật tài liệu
- `style:` - Format code, không thay đổi logic
- `refactor:` - Refactor code
- `test:` - Thêm/sửa tests
- `chore:` - Cập nhật build, dependencies

### 5. Push và Pull Request

```bash
# Push lên GitHub
git push origin feature/ten-tinh-nang

# Tạo Pull Request trên GitHub
```

## 📋 Quy tắc Code

### Python Code Style

- Tuân thủ PEP 8
- Sử dụng 4 spaces cho indentation
- Tên biến/hàm: `snake_case`
- Tên class: `PascalCase`
- Docstrings cho functions/classes

```python
def sign_jar(jar_file, keystore):
    """Ký file JAR với certificate
    
    Args:
        jar_file: Đường dẫn đến file JAR
        keystore: Đường dẫn đến keystore
        
    Returns:
        bool: True nếu thành công
    """
    pass
```

### Shell Script Style

- Sử dụng `#!/bin/bash` hoặc `#!/usr/bin/env bash`
- Thêm comments giải thích
- Kiểm tra errors với `set -e`
- Sử dụng quotes cho variables

```bash
#!/bin/bash
set -e

# Ký file JAR
sign_jar() {
    local jar_file="$1"
    echo "Signing ${jar_file}..."
}
```

## 🧪 Testing

Trước khi submit PR, hãy test:

1. **GUI Application**
   ```bash
   python s40_sign_app.py
   ```
   - Test tất cả tabs
   - Test đổi ngôn ngữ
   - Test các chức năng chính

2. **Command Line Tool**
   ```bash
   python sign_tool.py --create-cert
   python sign_tool.py --sign test.jar
   ```

3. **Windows Script**
   ```bash
   s40tool.bat
   ```
   - Test tất cả menu options

4. **Shell Scripts** (Linux/Mac)
   ```bash
   ./create_cert.sh
   ./sign_jar.sh test.jar
   ```

## 🐛 Báo cáo Bug

Khi báo cáo bug, vui lòng cung cấp:

1. **Mô tả bug** - Mô tả rõ ràng, ngắn gọn
2. **Các bước tái hiện**
   - Bước 1: ...
   - Bước 2: ...
   - Kết quả: ...
3. **Kết quả mong đợi** - Bạn mong đợi điều gì xảy ra
4. **Screenshots** - Nếu có
5. **Môi trường**
   - OS: Windows 10 / Ubuntu 22.04 / macOS 13
   - Python version: 3.9.0
   - Java version: JDK 11

## 💡 Đề xuất tính năng

Khi đề xuất tính năng mới:

1. **Mô tả tính năng** - Giải thích rõ ràng
2. **Use case** - Tại sao cần tính năng này?
3. **Giải pháp đề xuất** - Bạn nghĩ nên implement như thế nào?
4. **Alternatives** - Có cách nào khác không?

## 📝 Cập nhật Documentation

Nếu thay đổi code, hãy cập nhật:

- `README.md` - Nếu thêm tính năng mới
- Docstrings trong code
- Comments giải thích logic phức tạp

## ✅ Checklist trước khi Submit PR

- [ ] Code chạy được không lỗi
- [ ] Đã test trên môi trường local
- [ ] Code tuân thủ style guide
- [ ] Đã thêm/cập nhật comments
- [ ] Đã cập nhật documentation nếu cần
- [ ] Commit messages rõ ràng
- [ ] Không commit files nhạy cảm (certificates, passwords)

## 🤝 Code Review

Sau khi submit PR:

1. Maintainer sẽ review code
2. Có thể yêu cầu thay đổi
3. Sau khi approve, PR sẽ được merge

## 📞 Liên hệ

- GitHub Issues: [Link to issues]
- Email: support@example.com

## 🙏 Cảm ơn!

Mọi đóng góp đều được trân trọng! 

---

**Happy Coding!** 🚀
