#!/bin/bash
# Script tạo certificate cho S40 Java App (Linux/Mac)

echo "========================================"
echo "S40 Certificate Generator"
echo "========================================"
echo

# Tạo thư mục certs nếu chưa có
mkdir -p certs

# Thông tin certificate
KEYSTORE="certs/s40-keystore.jks"
ALIAS="s40cert"
STOREPASS="s40pass123"
KEYPASS="s40pass123"
VALIDITY=3650
KEYALG="RSA"
KEYSIZE=2048

echo "Đang tạo keystore và certificate..."
echo

# Tạo keystore và certificate
keytool -genkeypair \
    -alias "$ALIAS" \
    -keyalg "$KEYALG" \
    -keysize $KEYSIZE \
    -validity $VALIDITY \
    -keystore "$KEYSTORE" \
    -storepass "$STOREPASS" \
    -keypass "$KEYPASS" \
    -dname "CN=S40 Developer, OU=Mobile Dev, O=MyCompany, L=Hanoi, ST=Hanoi, C=VN"

if [ $? -eq 0 ]; then
    echo
    echo "========================================"
    echo "Tạo certificate thành công!"
    echo "========================================"
    echo "Keystore: $KEYSTORE"
    echo "Alias: $ALIAS"
    echo "Password: $STOREPASS"
    echo
    echo "Xem thông tin certificate:"
    echo "keytool -list -v -keystore $KEYSTORE -storepass $STOREPASS"
else
    echo
    echo "Lỗi: Không thể tạo certificate!"
    echo "Vui lòng kiểm tra Java JDK đã được cài đặt."
fi

echo
