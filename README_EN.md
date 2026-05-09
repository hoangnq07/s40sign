# S40 Certificate & Signing Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey.svg)](https://github.com)

A comprehensive tool for creating certificates and signing Java applications for Nokia Series 40 (S40) phones.

[🇻🇳 Tiếng Việt](README.md) | [🇬🇧 English](README_EN.md)

## ✨ Features

- 🖥️ **GUI Application** - User-friendly graphical interface
- 🌍 **Multi-language** - Vietnamese and English support
- 🔐 **Certificate Creation** - Self-signed certificates for S40
- ✍️ **JAR Signing** - Sign Java ME applications
- 🔄 **Auto Signature Removal** - Intelligent handling of old signatures
- 📦 **Standalone .exe** - No Python installation required
- 🛠️ **Command Line Tools** - Scripts for automation
- 🎨 **Instant Language Switching** - <0.1s switching time

## 🚀 Quick Start

### Option 1: Run .exe (Easiest - Windows)

```bash
# Double-click or run
dist\S40SignTool.exe
```

**Requirements:**
- ✅ Windows 7+
- ✅ Java JDK 8+

**Not Required:**
- ❌ Python
- ❌ Libraries

### Option 2: All-in-One Script (Windows)

```bash
# Run interactive menu
s40tool.bat
```

Menu includes:
1. Run GUI Application
2. Create Certificate
3. Sign JAR File
4. Remove Signature
5. Manage Certificate
6. Build .exe
7. Exit

### Option 3: Python GUI

```bash
# Windows
python s40_sign_app.py

# Linux/Mac
chmod +x run_app.sh
./run_app.sh
```

### Option 4: Command Line (Linux/Mac)

```bash
# Create certificate
./create_cert.sh

# Sign JAR
./sign_jar.sh apps/MyApp.jar

# Manage certificate
./manage_cert.sh
```

## 📋 System Requirements

### Required
- **Java JDK 8+** (includes keytool and jarsigner)
  - Download: https://www.oracle.com/java/technologies/downloads/

### Optional (only for Python source)
- **Python 3.6+** (if running from source)
  - Download: https://www.python.org/downloads/

## 📁 Project Structure

```
SignS40/
├── dist/
│   └── S40SignTool.exe          # ⭐ GUI Application (Windows)
│
├── s40tool.bat                  # ⭐ All-in-one script (Windows)
├── s40_sign_app.py              # GUI application (Python)
├── sign_tool.py                 # CLI tool (Python)
│
├── create_cert.sh               # Create certificate (Linux/Mac)
├── sign_jar.sh                  # Sign JAR (Linux/Mac)
├── manage_cert.sh               # Manage certificate (Linux/Mac)
├── remove_signature.sh          # Remove signature (Linux/Mac)
├── run_app.sh                   # Run GUI (Linux/Mac)
│
├── README.md                    # Documentation (Vietnamese)
├── README_EN.md                 # Documentation (English)
├── CONTRIBUTING.md              # Contribution guidelines
├── CHANGELOG.md                 # Version history
├── LICENSE                      # MIT License
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
├── .gitattributes               # Git attributes
│
├── certs/                       # Certificates (auto-created)
└── apps/                        # Apps to sign (auto-created)
```

## 🎯 Usage Guide

### 1. Create Certificate (First Time)

**GUI:**
- Open "Manage Certificate" tab
- Click "Create Certificate"

**Command Line:**
```bash
# Windows
s40tool.bat
# Select option 2

# Linux/Mac
./create_cert.sh
```

### 2. Sign JAR Application

**GUI:**
- "Sign JAR" tab
- Select JAR file
- Click "Sign JAR"

**Command Line:**
```bash
# Windows
s40tool.bat
# Select option 3

# Linux/Mac
./sign_jar.sh apps/MyApp.jar
```

### 3. Change Language (GUI)

- Find "Language" dropdown in top right
- Select: 🇻🇳 Tiếng Việt or 🇬🇧 English
- UI updates instantly

## 🔧 Default Configuration

- **Keystore:** `certs/s40-keystore.jks`
- **Alias:** `s40cert`
- **Password:** `s40pass123`
- **Validity:** 3650 days (10 years)
- **Algorithm:** RSA 2048-bit

⚠️ **Note:** Change password in production!

## 📦 Build .exe from Source

```bash
# Windows
s40tool.bat
# Select option 6

# Or manually
pip install pyinstaller
pyinstaller --onefile --windowed --name "S40SignTool" s40_sign_app.py
```

Result: `dist\S40SignTool.exe`

## 🐛 Troubleshooting

### Error: "Java not found"

**Solution:**
1. Install Java JDK
2. Add Java to PATH
3. Restart terminal

### Error: "Keystore not found"

**Solution:**
- Create certificate first (Option 2 in menu)

### Error: "Cannot sign JAR"

**Solution:**
1. Check JAR file is valid
2. Recreate certificate
3. Try signing again

## 🌟 Key Features

✅ **Ready-to-use .exe** - No Python installation needed!  
✅ **Multi-language** - Vietnamese and English  
✅ **All-in-one script** - Single .bat file for everything  
✅ **Auto old signature handling** - Intelligent  
✅ **Intuitive GUI** - Easy to use  
✅ **Command line tools** - For automation  
✅ **Cross-platform** - Windows, Linux, Mac  
✅ **Auto backup** - Safe operations  

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 📞 Support

- **GitHub Issues:** [Report bugs or request features]
- **Email:** support@example.com

## 🙏 Acknowledgments

- Built with Python + Tkinter
- Uses Java JDK tools (keytool, jarsigner)
- Designed for Nokia Series 40 developers

## 📊 Statistics

- **Lines of Code:** ~2,700+
- **Languages:** Python, Shell, Batch
- **Platforms:** Windows, Linux, macOS
- **File Size:** ~11 MB (standalone .exe)

---

**Version:** 1.1.1  
**Last Updated:** May 10, 2026  
**Status:** ✅ Ready for production!

Made with ❤️ for S40 developers

