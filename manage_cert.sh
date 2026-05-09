#!/bin/bash
# Script quản lý certificate cho S40 Java App (Linux/Mac)

KEYSTORE="certs/s40-keystore.jks"
ALIAS="s40cert"
STOREPASS="s40pass123"

show_menu() {
    clear
    echo "========================================"
    echo "S40 Certificate Manager"
    echo "========================================"
    echo
    echo "1. Xem thông tin certificate"
    echo "2. Kiểm tra hạn sử dụng certificate"
    echo "3. Xóa certificate cũ"
    echo "4. Tạo certificate mới"
    echo "5. Xuất certificate ra file"
    echo "6. Đổi password keystore"
    echo "7. Thoát"
    echo
    read -p "Chọn chức năng (1-7): " choice
    
    case $choice in
        1) view_cert ;;
        2) check_expiry ;;
        3) delete_cert ;;
        4) create_cert ;;
        5) export_cert ;;
        6) change_password ;;
        7) exit 0 ;;
        *) echo "Lựa chọn không hợp lệ!"; sleep 2; show_menu ;;
    esac
}

view_cert() {
    echo
    echo "========================================"
    echo "Thông tin Certificate"
    echo "========================================"
    echo
    
    if [ ! -f "$KEYSTORE" ]; then
        echo "Không tìm thấy keystore!"
        read -p "Nhấn Enter để tiếp tục..."
        show_menu
        return
    fi
    
    keytool -list -v -keystore "$KEYSTORE" -storepass "$STOREPASS" -alias "$ALIAS"
    echo
    read -p "Nhấn Enter để tiếp tục..."
    show_menu
}

check_expiry() {
    echo
    echo "========================================"
    echo "Kiểm tra hạn sử dụng"
    echo "========================================"
    echo
    
    if [ ! -f "$KEYSTORE" ]; then
        echo "Không tìm thấy keystore!"
        read -p "Nhấn Enter để tiếp tục..."
        show_menu
        return
    fi
    
    keytool -list -v -keystore "$KEYSTORE" -storepass "$STOREPASS" -alias "$ALIAS" | grep "Valid from"
    echo
    read -p "Nhấn Enter để tiếp tục..."
    show_menu
}

delete_cert() {
    echo
    echo "========================================"
    echo "Xóa Certificate"
    echo "========================================"
    echo
    
    if [ ! -f "$KEYSTORE" ]; then
        echo "Không tìm thấy keystore!"
        read -p "Nhấn Enter để tiếp tục..."
        show_menu
        return
    fi
    
    read -p "Bạn có chắc chắn muốn xóa certificate? (y/N): " confirm
    if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
        echo "Đã hủy."
        read -p "Nhấn Enter để tiếp tục..."
        show_menu
        return
    fi
    
    keytool -delete -alias "$ALIAS" -keystore "$KEYSTORE" -storepass "$STOREPASS"
    if [ $? -eq 0 ]; then
        echo "Đã xóa certificate thành công!"
    else
        echo "Lỗi khi xóa certificate!"
    fi
    
    read -p "Nhấn Enter để tiếp tục..."
    show_menu
}

create_cert() {
    echo
    echo "========================================"
    echo "Tạo Certificate Mới"
    echo "========================================"
    echo
    
    ./create_cert.sh
    read -p "Nhấn Enter để tiếp tục..."
    show_menu
}

export_cert() {
    echo
    echo "========================================"
    echo "Xuất Certificate"
    echo "========================================"
    echo
    
    if [ ! -f "$KEYSTORE" ]; then
        echo "Không tìm thấy keystore!"
        read -p "Nhấn Enter để tiếp tục..."
        show_menu
        return
    fi
    
    CERT_FILE="certs/s40-cert.cer"
    keytool -exportcert -alias "$ALIAS" -keystore "$KEYSTORE" -storepass "$STOREPASS" -file "$CERT_FILE"
    
    if [ $? -eq 0 ]; then
        echo "Đã xuất certificate thành công!"
        echo "File: $CERT_FILE"
    else
        echo "Lỗi khi xuất certificate!"
    fi
    
    read -p "Nhấn Enter để tiếp tục..."
    show_menu
}

change_password() {
    echo
    echo "========================================"
    echo "Đổi Password Keystore"
    echo "========================================"
    echo
    
    if [ ! -f "$KEYSTORE" ]; then
        echo "Không tìm thấy keystore!"
        read -p "Nhấn Enter để tiếp tục..."
        show_menu
        return
    fi
    
    echo "Lưu ý: Bạn cần cập nhật password mới trong các script!"
    echo
    
    read -sp "Nhập password cũ: " oldpass
    echo
    read -sp "Nhập password mới: " newpass
    echo
    read -sp "Nhập lại password mới: " newpass2
    echo
    
    if [ "$newpass" != "$newpass2" ]; then
        echo "Password không khớp!"
        read -p "Nhấn Enter để tiếp tục..."
        show_menu
        return
    fi
    
    keytool -storepasswd -keystore "$KEYSTORE" -storepass "$oldpass" -new "$newpass"
    if [ $? -eq 0 ]; then
        echo "Đã đổi password keystore thành công!"
        echo
        echo "Đổi password của key:"
        keytool -keypasswd -alias "$ALIAS" -keystore "$KEYSTORE" -storepass "$newpass" -keypass "$oldpass" -new "$newpass"
        if [ $? -eq 0 ]; then
            echo "Đã đổi password key thành công!"
            echo
            echo "LƯU Ý: Cập nhật password mới trong các script:"
            echo "- create_cert.sh"
            echo "- sign_jar.sh"
            echo "- sign_tool.py"
        fi
    else
        echo "Lỗi khi đổi password!"
    fi
    
    read -p "Nhấn Enter để tiếp tục..."
    show_menu
}

# Main
show_menu
