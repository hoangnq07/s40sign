#!/bin/bash
# Script xóa chữ ký khỏi JAR file (Linux/Mac)

echo "========================================"
echo "S40 Signature Remover"
echo "========================================"
echo

# Kiểm tra tham số
if [ -z "$1" ]; then
    echo "Sử dụng: ./remove_signature.sh path/to/app.jar"
    echo
    exit 1
fi

JAR_FILE="$1"

# Kiểm tra file JAR tồn tại
if [ ! -f "$JAR_FILE" ]; then
    echo "Lỗi: Không tìm thấy file $JAR_FILE"
    echo
    exit 1
fi

# Kiểm tra chữ ký
if ! jarsigner -verify "$JAR_FILE" >/dev/null 2>&1; then
    echo "File JAR không có chữ ký."
    echo
    exit 0
fi

echo "Phát hiện chữ ký trong JAR."
echo "Đang xóa chữ ký..."
echo

# Tạo thư mục tạm
TEMP_DIR=$(mktemp -d)

# Giải nén JAR
unzip -q "$JAR_FILE" -d "$TEMP_DIR"

# Xóa các file chữ ký
rm -f "$TEMP_DIR/META-INF/"*.SF
rm -f "$TEMP_DIR/META-INF/"*.RSA
rm -f "$TEMP_DIR/META-INF/"*.DSA

# Tạo backup
BACKUP_FILE="${JAR_FILE}.bak"
cp "$JAR_FILE" "$BACKUP_FILE"

# Nén lại thành JAR
cd "$TEMP_DIR"
jar cf "$JAR_FILE" *
cd - >/dev/null

# Dọn dẹp
rm -rf "$TEMP_DIR"

echo "========================================"
echo "Đã xóa chữ ký thành công!"
echo "========================================"
echo "File gốc: $JAR_FILE"
echo "Backup: $BACKUP_FILE"
echo

# Xác minh
if jarsigner -verify "$JAR_FILE" 2>&1 | grep -q "jar is unsigned"; then
    echo "✓ JAR đã không còn chữ ký."
else
    echo "⚠ Cảnh báo: JAR vẫn còn chữ ký!"
fi

echo
