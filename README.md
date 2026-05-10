# S40 Certificate & Signing Tool

Công cụ tạo certificate và ký ứng dụng Java cho điện thoại S40 (Series 40).

## ✨ Tính năng

- 🖥️ **Ứng dụng GUI** - Giao diện đồ họa dễ sử dụng
- 🌍 **Đa ngôn ngữ** - Tiếng Việt và English
- 🔐 **Tạo certificate** - Certificate tự ký cho S40
- ✍️ **Ký JAR** - Ký ứng dụng Java ME
- 🔄 **Tự động xóa chữ ký cũ** - Xử lý thông minh
- 📦 **File .exe sẵn sàng** - Không cần cài Python
- 🛠️ **Command line tools** - Scripts cho automation

## 🚀 Quick Start

### Cách 1: Chạy file .exe (Đơn giản nhất - Windows)

```bash
# Double-click hoặc
dist\S40SignTool.exe
```

**Yêu cầu:**
- ✅ Windows 7+
- ✅ Java JDK 8+

**Không cần:**
- ❌ Python
- ❌ Thư viện

### Cách 2: Sử dụng All-in-One Script (Windows)

```bash
# Chạy menu tương tác
s40tool.bat
```

Menu bao gồm:
1. Run GUI Application
2. Create Certificate
3. Sign JAR File
4. Remove Signature
5. Manage Certificate
6. Build .exe
7. Exit

### Cách 3: Python GUI

```bash
# Windows
python s40_sign_app.py

# Linux/Mac
chmod +x run_app.sh
./run_app.sh
```

### Cách 4: Command Line (Linux/Mac)

```bash
# Tạo certificate
./create_cert.sh

# Ký JAR
./sign_jar.sh apps/MyApp.jar

# Quản lý certificate
./manage_cert.sh
```

## 📋 Yêu cầu hệ thống

### Bắt buộc
- **Java JDK 8+** (có keytool và jarsigner)
  - Download: https://www.oracle.com/java/technologies/downloads/

### Tùy chọn (chỉ khi dùng Python)
- **Python 3.6+** (nếu chạy từ source)
  - Download: https://www.python.org/downloads/

## 📁 Cấu trúc dự án

```
s40-cert-tool/
├── dist/
│   └── S40SignTool.exe          # ⭐ Ứng dụng GUI (Windows)
│
├── s40tool.bat                  # ⭐ All-in-one script (Windows)
├── s40_sign_app.py              # GUI application (Python)
├── sign_tool.py                 # CLI tool (Python)
│
├── create_cert.sh               # Tạo certificate (Linux/Mac)
├── sign_jar.sh                  # Ký JAR (Linux/Mac)
├── manage_cert.sh               # Quản lý cert (Linux/Mac)
├── remove_signature.sh          # Xóa chữ ký (Linux/Mac)
├── run_app.sh                   # Chạy GUI (Linux/Mac)
│
├── README.md                    # Tài liệu này
├── requirements.txt             # Python dependencies
├── .gitignore
│
├── certs/                       # Certificates (tự động tạo)
└── apps/                        # Ứng dụng cần ký (tự động tạo)
```

## 🎯 Hướng dẫn sử dụng

### 1. Tạo Certificate (lần đầu)

**GUI:**
- Mở tab "Quản lý Certificate" / "Manage Certificate"
- Click "Tạo Certificate" / "Create Certificate"

**Command Line:**
```bash
# Windows
s40tool.bat
# Chọn option 2

# Linux/Mac
./create_cert.sh
```

### 2. Ký ứng dụng JAR

**GUI:**
- Tab "Ký JAR" / "Sign JAR"
- Chọn file JAR
- Click "Ký JAR" / "Sign JAR"

**Command Line:**
```bash
# Windows
s40tool.bat
# Chọn option 3

# Linux/Mac
./sign_jar.sh apps/MyApp.jar
```

### 3. Xuất Certificate cho Nokia S40

**GUI:**
- Tab "Quản lý Certificate" / "Manage Certificate"
- Click "Xuất Certificate (.cer + .der)" / "Export Certificate (.cer + .der)"
- Chọn thư mục để lưu (mặc định: `certs`)
- App sẽ tự động tạo **2 file**:
  - `my_nokia_cert.cer` - Certificate format (khuyến nghị)
  - `my_nokia_cert.der` - DER format (tương thích rộng)

**💡 Lưu ý:** Cả 2 file đều giống nhau về nội dung, chỉ khác tên. Bạn chỉ cần dùng **1 trong 2 file** để cài vào điện thoại.

**Cài vào điện thoại Nokia S40:**

**Cách 1: Qua Bluetooth** (Khuyến nghị - Dễ nhất)
1. Gửi file `.cer` hoặc `.der` qua Bluetooth từ máy tính/điện thoại khác
2. Nhận file trên Nokia S40
3. Mở file → Điện thoại tự động cài đặt certificate

**Cách 2: Qua thẻ nhớ**
1. Copy file `.cer` hoặc `.der` vào thẻ nhớ (dùng card reader)
2. Lắp thẻ nhớ vào điện thoại
3. File Manager → Tìm file → Mở
4. Điện thoại tự động cài đặt

**Cách 3: Qua USB (Mass Storage)**
1. Kết nối điện thoại qua USB
2. Chọn chế độ "Mass Storage" trên điện thoại
3. Copy file vào thẻ nhớ điện thoại
4. Rút USB → File Manager → Mở file

**Kiểm tra certificate đã cài:**
- Menu → Settings → Security → Certificate Management
- Sẽ thấy certificate của bạn trong danh sách

### 4. Đổi ngôn ngữ (GUI)

- Tìm dropdown "Language" ở góc trên phải
- Chọn: 🇻🇳 Tiếng Việt hoặc 🇬🇧 English
- Giao diện cập nhật ngay lập tức

## 🔧 Cấu hình mặc định

- **Keystore:** `certs/s40-keystore.jks`
- **Alias:** `s40cert`
- **Password:** `s40pass123`
- **Validity:** 3650 ngày (10 năm)

⚠️ **Lưu ý:** Đổi password trong production!

## 📦 Build .exe từ source

```bash
# Windows
s40tool.bat
# Chọn option 6

# Hoặc thủ công
pip install pyinstaller
pyinstaller --onefile --windowed --name "S40SignTool" s40_sign_app.py
```

Kết quả: `dist\S40SignTool.exe`

## 🐛 Xử lý lỗi

### Lỗi: "Java not found"

**Giải pháp:**
1. Cài Java JDK
2. Thêm Java vào PATH
3. Khởi động lại terminal

### Lỗi: "Keystore not found"

**Giải pháp:**
- Tạo certificate trước (Option 2 trong menu)

### Lỗi: "Cannot sign JAR"

**Giải pháp:**
1. Kiểm tra file JAR hợp lệ
2. Tạo lại certificate
3. Thử ký lại

## 🌟 Tính năng nổi bật

✅ **File .exe sẵn sàng** - Không cần cài Python!  
✅ **Đa ngôn ngữ** - Tiếng Việt và English  
✅ **All-in-one script** - Một file .bat cho tất cả  
✅ **Tự động xử lý chữ ký cũ** - Thông minh  
✅ **GUI trực quan** - Dễ sử dụng  
✅ **Command line tools** - Cho automation  
✅ **Đa nền tảng** - Windows, Linux, Mac  
✅ **Backup tự động** - An toàn  

## 📞 Hỗ trợ

- **GitHub Issues:** [Link]
- **Email:** support@example.com

## 📄 License

© 2026 - S40 Sign Tool  
Developed with Python + Tkinter

## 🔗 GitHub

Repository: https://github.com/hoangnq07/s40sign

### Clone project
```bash
git clone https://github.com/hoangnq07/s40sign.git
cd s40sign
```

### Download .exe
Vào [Releases](https://github.com/hoangnq07/s40sign/releases) để tải file .exe

---

**Version:** 1.1.1  
**Last Updated:** May 10, 2026  
**Status:** ✅ Ready for use!
