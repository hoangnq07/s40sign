#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S40 Java App Certificate & Signing Tool
Công cụ tạo certificate và ký ứng dụng Java cho điện thoại S40
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path


class S40SignTool:
    """Công cụ ký ứng dụng S40"""
    
    def __init__(self):
        self.keystore = "certs/s40-keystore.jks"
        self.alias = "s40cert"
        self.storepass = "s40pass123"
        self.keypass = "s40pass123"
        self.validity = 3650
        self.keyalg = "RSA"
        self.keysize = 2048
        
    def create_certificate(self):
        """Tạo certificate mới"""
        print("=" * 50)
        print("S40 Certificate Generator")
        print("=" * 50)
        print()
        
        # Tạo thư mục certs
        Path("certs").mkdir(exist_ok=True)
        
        # Kiểm tra keystore đã tồn tại
        if os.path.exists(self.keystore):
            response = input(f"Keystore {self.keystore} đã tồn tại. Ghi đè? (y/N): ")
            if response.lower() != 'y':
                print("Hủy bỏ.")
                return False
        
        print("Đang tạo keystore và certificate...")
        print()
        
        # Lệnh tạo certificate
        cmd = [
            "keytool", "-genkeypair",
            "-alias", self.alias,
            "-keyalg", self.keyalg,
            "-keysize", str(self.keysize),
            "-validity", str(self.validity),
            "-keystore", self.keystore,
            "-storepass", self.storepass,
            "-keypass", self.keypass,
            "-dname", "CN=S40 Developer, OU=Mobile Dev, O=MyCompany, L=Hanoi, ST=Hanoi, C=VN"
        ]
        
        try:
            subprocess.run(cmd, check=True)
            print()
            print("=" * 50)
            print("Tạo certificate thành công!")
            print("=" * 50)
            print(f"Keystore: {self.keystore}")
            print(f"Alias: {self.alias}")
            print(f"Password: {self.storepass}")
            print()
            print("Xem thông tin certificate:")
            print(f"keytool -list -v -keystore {self.keystore} -storepass {self.storepass}")
            return True
        except subprocess.CalledProcessError:
            print()
            print("Lỗi: Không thể tạo certificate!")
            print("Vui lòng kiểm tra Java JDK đã được cài đặt.")
            return False
        except FileNotFoundError:
            print()
            print("Lỗi: Không tìm thấy lệnh 'keytool'!")
            print("Vui lòng cài đặt Java JDK và thêm vào PATH.")
            return False
    
    def remove_signature(self, jar_file):
        """Xóa chữ ký cũ khỏi JAR"""
        import zipfile
        import tempfile
        import shutil
        
        print("Đang xóa chữ ký cũ...")
        
        # Tạo file tạm
        temp_jar = jar_file + ".tmp"
        
        try:
            # Đọc JAR gốc và loại bỏ các file chữ ký
            with zipfile.ZipFile(jar_file, 'r') as zip_in:
                with zipfile.ZipFile(temp_jar, 'w', zipfile.ZIP_DEFLATED) as zip_out:
                    for item in zip_in.infolist():
                        # Bỏ qua các file chữ ký trong META-INF
                        if item.filename.startswith('META-INF/') and (
                            item.filename.endswith('.SF') or
                            item.filename.endswith('.RSA') or
                            item.filename.endswith('.DSA')
                        ):
                            continue
                        
                        # Copy các file khác
                        data = zip_in.read(item.filename)
                        zip_out.writestr(item, data)
            
            # Thay thế file gốc
            shutil.move(temp_jar, jar_file)
            print("Đã xóa chữ ký cũ thành công.")
            return True
            
        except Exception as e:
            print(f"Lỗi khi xóa chữ ký: {e}")
            if os.path.exists(temp_jar):
                os.remove(temp_jar)
            return False
    
    def check_signature(self, jar_file):
        """Kiểm tra xem JAR có chữ ký không"""
        cmd = ["jarsigner", "-verify", jar_file]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            return result.returncode == 0
        except:
            return False
    
    def sign_jar(self, jar_file, force_resign=True):
        """Ký file JAR
        
        Args:
            jar_file: Đường dẫn đến file JAR
            force_resign: Nếu True, tự động xóa chữ ký cũ và ký lại
        """
        print("=" * 50)
        print("S40 JAR Signer")
        print("=" * 50)
        print()
        
        # Kiểm tra file JAR
        if not os.path.exists(jar_file):
            print(f"Lỗi: Không tìm thấy file {jar_file}")
            return False
        
        # Kiểm tra keystore
        if not os.path.exists(self.keystore):
            print(f"Lỗi: Không tìm thấy keystore {self.keystore}")
            print("Vui lòng tạo certificate trước: python sign_tool.py --create-cert")
            return False
        
        # Kiểm tra chữ ký cũ
        if self.check_signature(jar_file):
            print("⚠️  Phát hiện JAR đã có chữ ký.")
            if force_resign:
                print("Đang xóa chữ ký cũ và ký lại...")
                if not self.remove_signature(jar_file):
                    return False
            else:
                response = input("Xóa chữ ký cũ và ký lại? (y/N): ")
                if response.lower() != 'y':
                    print("Hủy bỏ.")
                    return False
                if not self.remove_signature(jar_file):
                    return False
        
        # Tạo tên file output
        jar_path = Path(jar_file)
        signed_jar = jar_path.parent / f"{jar_path.stem}-signed{jar_path.suffix}"
        
        print()
        print(f"Đang ký file JAR...")
        print(f"Input: {jar_file}")
        print(f"Output: {signed_jar}")
        print()
        
        # Lệnh ký JAR
        cmd = [
            "jarsigner",
            "-keystore", self.keystore,
            "-storepass", self.storepass,
            "-keypass", self.keypass,
            "-signedjar", str(signed_jar),
            jar_file,
            self.alias
        ]
        
        try:
            subprocess.run(cmd, check=True)
            print()
            print("=" * 50)
            print("Ký JAR thành công!")
            print("=" * 50)
            print(f"File đã ký: {signed_jar}")
            print()
            print("Xác minh chữ ký:")
            print(f'jarsigner -verify -verbose -certs "{signed_jar}"')
            print()
            
            # Cập nhật file JAD nếu có
            jad_file = jar_path.parent / f"{jar_path.stem}.jad"
            if jad_file.exists():
                print(f"Tìm thấy file JAD: {jad_file}")
                print("Đang cập nhật thông tin JAD...")
                self.update_jad(jad_file, signed_jar)
            
            return True
        except subprocess.CalledProcessError:
            print()
            print("Lỗi: Không thể ký file JAR!")
            return False
        except FileNotFoundError:
            print()
            print("Lỗi: Không tìm thấy lệnh 'jarsigner'!")
            print("Vui lòng cài đặt Java JDK và thêm vào PATH.")
            return False
    
    def update_jad(self, jad_file, signed_jar):
        """Cập nhật file JAD với thông tin JAR đã ký"""
        jad_path = Path(jad_file)
        signed_jad = jad_path.parent / f"{jad_path.stem}-signed{jad_path.suffix}"
        
        # Lấy kích thước file JAR
        jar_size = os.path.getsize(signed_jar)
        
        # Đọc nội dung JAD gốc
        with open(jad_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Cập nhật hoặc thêm thông tin
        lines = content.split('\n')
        updated = False
        
        for i, line in enumerate(lines):
            if line.startswith('MIDlet-Jar-Size:'):
                lines[i] = f'MIDlet-Jar-Size: {jar_size}'
                updated = True
            elif line.startswith('MIDlet-Jar-URL:'):
                lines[i] = f'MIDlet-Jar-URL: {Path(signed_jar).name}'
        
        if not updated:
            lines.append(f'MIDlet-Jar-Size: {jar_size}')
            lines.append(f'MIDlet-Jar-URL: {Path(signed_jar).name}')
        
        # Ghi file JAD mới
        with open(signed_jad, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print(f"File JAD đã được tạo: {signed_jad}")
    
    def verify_jar(self, jar_file):
        """Xác minh chữ ký của file JAR"""
        print("=" * 50)
        print("S40 JAR Verifier")
        print("=" * 50)
        print()
        
        if not os.path.exists(jar_file):
            print(f"Lỗi: Không tìm thấy file {jar_file}")
            return False
        
        print(f"Đang xác minh: {jar_file}")
        print()
        
        cmd = ["jarsigner", "-verify", "-verbose", "-certs", jar_file]
        
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(result.stdout)
            print()
            print("=" * 50)
            print("Xác minh thành công!")
            print("=" * 50)
            return True
        except subprocess.CalledProcessError as e:
            print(e.stdout)
            print(e.stderr)
            print()
            print("Lỗi: File JAR không có chữ ký hợp lệ!")
            return False
        except FileNotFoundError:
            print("Lỗi: Không tìm thấy lệnh 'jarsigner'!")
            return False
    
    def list_keystore(self):
        """Liệt kê thông tin keystore"""
        print("=" * 50)
        print("Keystore Information")
        print("=" * 50)
        print()
        
        if not os.path.exists(self.keystore):
            print(f"Lỗi: Không tìm thấy keystore {self.keystore}")
            return False
        
        cmd = [
            "keytool", "-list", "-v",
            "-keystore", self.keystore,
            "-storepass", self.storepass
        ]
        
        try:
            subprocess.run(cmd, check=True)
            return True
        except subprocess.CalledProcessError:
            print("Lỗi: Không thể đọc keystore!")
            return False
        except FileNotFoundError:
            print("Lỗi: Không tìm thấy lệnh 'keytool'!")
            return False


def main():
    parser = argparse.ArgumentParser(
        description='S40 Java App Certificate & Signing Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ:
  Tạo certificate:
    python sign_tool.py --create-cert
  
  Ký file JAR (tự động xóa chữ ký cũ nếu có):
    python sign_tool.py --sign myapp.jar
  
  Ký lại file JAR (xóa chữ ký cũ và ký mới):
    python sign_tool.py --resign myapp.jar
  
  Chỉ xóa chữ ký (không ký lại):
    python sign_tool.py --remove-sig myapp.jar
  
  Xác minh chữ ký:
    python sign_tool.py --verify myapp-signed.jar
  
  Xem thông tin keystore:
    python sign_tool.py --list
        """
    )
    
    parser.add_argument('--create-cert', action='store_true',
                        help='Tạo certificate mới')
    parser.add_argument('--sign', metavar='JAR_FILE',
                        help='Ký file JAR')
    parser.add_argument('--resign', metavar='JAR_FILE',
                        help='Xóa chữ ký cũ và ký lại file JAR')
    parser.add_argument('--remove-sig', metavar='JAR_FILE',
                        help='Chỉ xóa chữ ký khỏi JAR (không ký lại)')
    parser.add_argument('--verify', metavar='JAR_FILE',
                        help='Xác minh chữ ký của file JAR')
    parser.add_argument('--list', action='store_true',
                        help='Liệt kê thông tin keystore')
    
    args = parser.parse_args()
    
    # Nếu không có tham số, hiển thị help
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    tool = S40SignTool()
    
    if args.create_cert:
        tool.create_certificate()
    elif args.sign:
        tool.sign_jar(args.sign, force_resign=True)
    elif args.resign:
        tool.sign_jar(args.resign, force_resign=True)
    elif args.remove_sig:
        if tool.check_signature(args.remove_sig):
            tool.remove_signature(args.remove_sig)
            print("Đã xóa chữ ký thành công!")
        else:
            print("File JAR không có chữ ký.")
    elif args.verify:
        tool.verify_jar(args.verify)
    elif args.list:
        tool.list_keystore()


if __name__ == '__main__':
    main()
