#!/bin/bash
# Script ký JAR file cho S40 Java App (Linux/Mac)

echo "========================================"
echo "S40 JAR Signer"
echo "========================================"
echo

# Kiểm tra tham số
if [ -z "$1" ]; then
    echo "Sử dụng: ./sign_jar.sh path/to/app.jar"
    echo
    exit 1
fi

JAR_FILE="$1"
KEYSTORE="certs/s40-keystore.jks"
ALIAS="s40cert"
STOREPASS="s40pass123"
KEYPASS="s40pass123"

# Kiểm tra file JAR tồn tại
if [ ! -f "$JAR_FILE" ]; then
    echo "Lỗi: Không tìm thấy file $JAR_FILE"
    echo
    exit 1
fi

# Kiểm tra keystore tồn tại
if [ ! -f "$KEYSTORE" ]; then
    echo "Lỗi: Không tìm thấy keystore $KEYSTORE"
    echo "Vui lòng chạy ./create_cert.sh trước!"
    echo
    exit 1
fi

# Tạo tên file output
JAR_DIR=$(dirname "$JAR_FILE")
JAR_NAME=$(basename "$JAR_FILE" .jar)
SIGNED_JAR="${JAR_DIR}/${JAR_NAME}-signed.jar"

echo "Kiểm tra chữ ký cũ..."
if jarsigner -verify "$JAR_FILE" >/dev/null 2>&1; then
    echo "Phát hiện JAR đã có chữ ký. Đang xóa chữ ký cũ..."
    
    # Tạo thư mục tạm
    TEMP_DIR=$(mktemp -d)
    TEMP_JAR="${JAR_DIR}/${JAR_NAME}-temp.jar"
    
    # Giải nén JAR
    unzip -q "$JAR_FILE" -d "$TEMP_DIR"
    
    # Xóa các file chữ ký cũ
    rm -f "$TEMP_DIR/META-INF/"*.SF
    rm -f "$TEMP_DIR/META-INF/"*.RSA
    rm -f "$TEMP_DIR/META-INF/"*.DSA
    
    # Nén lại thành JAR mới
    cd "$TEMP_DIR"
    jar cf "$TEMP_JAR" *
    cd - >/dev/null
    
    # Dọn dẹp
    rm -rf "$TEMP_DIR"
    
    echo "Đã xóa chữ ký cũ thành công."
    JAR_FILE="$TEMP_JAR"
fi

echo
echo "Đang ký file JAR..."
echo "Input: $JAR_FILE"
echo "Output: $SIGNED_JAR"
echo

# Ký file JAR
jarsigner -keystore "$KEYSTORE" \
    -storepass "$STOREPASS" \
    -keypass "$KEYPASS" \
    -signedjar "$SIGNED_JAR" \
    "$JAR_FILE" \
    "$ALIAS"

# Xóa file tạm nếu có
if [ -f "${JAR_DIR}/${JAR_NAME}-temp.jar" ]; then
    rm -f "${JAR_DIR}/${JAR_NAME}-temp.jar"
fi

if [ $? -eq 0 ]; then
    echo
    echo "========================================"
    echo "Ký JAR thành công!"
    echo "========================================"
    echo "File đã ký: $SIGNED_JAR"
    echo
    echo "Xác minh chữ ký:"
    echo "jarsigner -verify -verbose -certs \"$SIGNED_JAR\""
    echo
    
    # Tạo file JAD nếu có
    JAD_FILE="${JAR_DIR}/${JAR_NAME}.jad"
    if [ -f "$JAD_FILE" ]; then
        echo "Tìm thấy file JAD: $JAD_FILE"
        echo "Đang cập nhật thông tin JAD..."
        update_jad "$JAD_FILE" "$SIGNED_JAR"
    fi
else
    echo
    echo "Lỗi: Không thể ký file JAR!"
    exit 1
fi

echo

update_jad() {
    local JAD="$1"
    local SIGNED="$2"
    local JAD_SIGNED="${JAD%.jad}-signed.jad"
    
    # Lấy kích thước file JAR đã ký
    local JAR_SIZE=$(stat -f%z "$SIGNED" 2>/dev/null || stat -c%s "$SIGNED" 2>/dev/null)
    
    # Copy và cập nhật JAD
    cp "$JAD" "$JAD_SIGNED"
    echo "MIDlet-Jar-Size: $JAR_SIZE" >> "$JAD_SIGNED"
    echo "MIDlet-Jar-URL: $(basename "$SIGNED")" >> "$JAD_SIGNED"
    
    echo "File JAD đã được tạo: $JAD_SIGNED"
}
