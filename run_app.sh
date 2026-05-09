#!/bin/bash
# Script chạy ứng dụng GUI

echo "Đang khởi động S40 Sign Tool..."
python3 s40_sign_app.py

if [ $? -ne 0 ]; then
    echo
    echo "Lỗi: Không thể chạy ứng dụng!"
    echo "Vui lòng kiểm tra Python đã được cài đặt."
fi
