#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S40 Certificate & Signing Tool - GUI Application
Ứng dụng GUI để tạo certificate và ký ứng dụng Java S40
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import sys
import subprocess
import threading
from pathlib import Path
import zipfile
from datetime import datetime
import json


# Language translations
TRANSLATIONS = {
    'vi': {
        'app_title': 'S40 Certificate & Signing Tool',
        'app_subtitle': 'Công cụ tạo certificate và ký ứng dụng Java cho điện thoại S40',
        'tab_sign': 'Ký JAR',
        'tab_cert': 'Quản lý Certificate',
        'tab_settings': 'Cài đặt',
        'select_jar': 'Chọn file JAR',
        'browse': 'Chọn file...',
        'options': 'Tùy chọn',
        'auto_remove_sig': 'Tự động xóa chữ ký cũ',
        'auto_update_jad': 'Tự động cập nhật file JAD',
        'sign_jar': 'Ký JAR',
        'remove_sig': 'Xóa chữ ký',
        'verify_sig': 'Xác minh chữ ký',
        'result': 'Kết quả',
        'cert_info': 'Thông tin Certificate',
        'create_cert': 'Tạo Certificate',
        'view_cert': 'Xem thông tin',
        'delete_cert': 'Xóa Certificate',
        'export_cert': 'Xuất Certificate',
        'keystore_config': 'Cấu hình Keystore',
        'keystore': 'Keystore',
        'alias': 'Alias',
        'password': 'Password',
        'cert_details': 'Thông tin Certificate',
        'cn': 'CN (Common Name)',
        'ou': 'OU (Organization Unit)',
        'o': 'O (Organization)',
        'l': 'L (Location)',
        'c': 'C (Country)',
        'save_settings': 'Lưu cài đặt',
        'about': 'Về ứng dụng',
        'about_text': 'S40 Certificate & Signing Tool v1.0\nCông cụ tạo certificate và ký ứng dụng Java cho điện thoại S40\n\n© 2026 - Phát triển bởi Python + Tkinter',
        'ready': 'Sẵn sàng',
        'java_ready': 'Java JDK đã sẵn sàng',
        'java_warning': 'Cảnh báo: Không tìm thấy Java JDK',
        'java_error': 'Lỗi: Không tìm thấy Java',
        'warning': 'Cảnh báo',
        'error': 'Lỗi',
        'success': 'Thành công',
        'confirm': 'Xác nhận',
        'select_jar_file': 'Vui lòng chọn file JAR!',
        'file_not_found': 'Không tìm thấy file',
        'keystore_not_found': 'Không tìm thấy keystore!\nVui lòng tạo certificate trước.',
        'signing_jar': 'Đang ký JAR...',
        'checking_old_sig': 'Kiểm tra chữ ký cũ...',
        'found_old_sig': 'Phát hiện chữ ký cũ. Đang xóa...',
        'removed_old_sig': 'Đã xóa chữ ký cũ thành công.',
        'sign_success': 'Ký JAR thành công!',
        'sign_error': 'Lỗi khi ký JAR!',
        'signed_file': 'File đã ký',
        'confirm_remove_sig': 'Bạn có chắc muốn xóa chữ ký khỏi file JAR này?',
        'removing_sig': 'Đang xóa chữ ký...',
        'remove_sig_success': 'Đã xóa chữ ký thành công!',
        'verifying': 'Đang xác minh...',
        'verify_success': 'Xác minh thành công!',
        'verify_failed': 'Xác minh thất bại!',
        'confirm_overwrite': 'Keystore đã tồn tại. Bạn có muốn ghi đè?',
        'creating_cert': 'Đang tạo certificate...',
        'create_cert_success': 'Tạo certificate thành công!',
        'create_cert_error': 'Không thể tạo certificate!',
        'reading_cert': 'Đang đọc thông tin certificate...',
        'confirm_delete_cert': 'Bạn có chắc muốn xóa certificate?',
        'deleting_cert': 'Đang xóa certificate...',
        'delete_cert_success': 'Đã xóa certificate!',
        'delete_cert_error': 'Không thể xóa certificate!',
        'save_cert': 'Lưu certificate',
        'exporting_cert': 'Đang xuất certificate...',
        'export_cert_success': 'Đã xuất certificate!',
        'export_cert_error': 'Không thể xuất certificate!',
        'settings_saved': 'Đã lưu cài đặt!',
        'language': 'Ngôn ngữ',
        'vietnamese': 'Tiếng Việt',
        'english': 'English',
    },
    'en': {
        'app_title': 'S40 Certificate & Signing Tool',
        'app_subtitle': 'Tool for creating certificates and signing Java apps for S40 phones',
        'tab_sign': 'Sign JAR',
        'tab_cert': 'Manage Certificate',
        'tab_settings': 'Settings',
        'select_jar': 'Select JAR file',
        'browse': 'Browse...',
        'options': 'Options',
        'auto_remove_sig': 'Automatically remove old signature',
        'auto_update_jad': 'Automatically update JAD file',
        'sign_jar': 'Sign JAR',
        'remove_sig': 'Remove Signature',
        'verify_sig': 'Verify Signature',
        'result': 'Result',
        'cert_info': 'Certificate Information',
        'create_cert': 'Create Certificate',
        'view_cert': 'View Info',
        'delete_cert': 'Delete Certificate',
        'export_cert': 'Export Certificate',
        'keystore_config': 'Keystore Configuration',
        'keystore': 'Keystore',
        'alias': 'Alias',
        'password': 'Password',
        'cert_details': 'Certificate Details',
        'cn': 'CN (Common Name)',
        'ou': 'OU (Organization Unit)',
        'o': 'O (Organization)',
        'l': 'L (Location)',
        'c': 'C (Country)',
        'save_settings': 'Save Settings',
        'about': 'About',
        'about_text': 'S40 Certificate & Signing Tool v1.0\nTool for creating certificates and signing Java apps for S40 phones\n\n© 2026 - Developed with Python + Tkinter',
        'ready': 'Ready',
        'java_ready': 'Java JDK is ready',
        'java_warning': 'Warning: Java JDK not found',
        'java_error': 'Error: Java not found',
        'warning': 'Warning',
        'error': 'Error',
        'success': 'Success',
        'confirm': 'Confirm',
        'select_jar_file': 'Please select a JAR file!',
        'file_not_found': 'File not found',
        'keystore_not_found': 'Keystore not found!\nPlease create a certificate first.',
        'signing_jar': 'Signing JAR...',
        'checking_old_sig': 'Checking old signature...',
        'found_old_sig': 'Found old signature. Removing...',
        'removed_old_sig': 'Old signature removed successfully.',
        'sign_success': 'JAR signed successfully!',
        'sign_error': 'Error signing JAR!',
        'signed_file': 'Signed file',
        'confirm_remove_sig': 'Are you sure you want to remove the signature from this JAR file?',
        'removing_sig': 'Removing signature...',
        'remove_sig_success': 'Signature removed successfully!',
        'verifying': 'Verifying...',
        'verify_success': 'Verification successful!',
        'verify_failed': 'Verification failed!',
        'confirm_overwrite': 'Keystore already exists. Do you want to overwrite it?',
        'creating_cert': 'Creating certificate...',
        'create_cert_success': 'Certificate created successfully!',
        'create_cert_error': 'Cannot create certificate!',
        'reading_cert': 'Reading certificate information...',
        'confirm_delete_cert': 'Are you sure you want to delete the certificate?',
        'deleting_cert': 'Deleting certificate...',
        'delete_cert_success': 'Certificate deleted!',
        'delete_cert_error': 'Cannot delete certificate!',
        'save_cert': 'Save certificate',
        'exporting_cert': 'Exporting certificate...',
        'export_cert_success': 'Certificate exported!',
        'export_cert_error': 'Cannot export certificate!',
        'settings_saved': 'Settings saved!',
        'language': 'Language',
        'vietnamese': 'Tiếng Việt',
        'english': 'English',
    }
}


class S40SignApp:
    """Ứng dụng GUI cho S40 Sign Tool"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("S40 Certificate & Signing Tool")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Language
        self.current_lang = 'vi'  # Default language
        self.load_language_preference()
        
        # Cấu hình
        self.keystore = "certs/s40-keystore.jks"
        self.alias = "s40cert"
        self.storepass = "s40pass123"
        self.keypass = "s40pass123"
        
        # Tạo thư mục cần thiết
        Path("certs").mkdir(exist_ok=True)
        Path("apps").mkdir(exist_ok=True)
        
        # Store widget references for language updates
        self.widgets = {}
        
        # Tạo giao diện
        self.create_widgets()
        
        # Kiểm tra Java
        self.check_java()
    
    def load_language_preference(self):
        """Load language preference from config file"""
        try:
            if os.path.exists('config.json'):
                with open('config.json', 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    self.current_lang = config.get('language', 'vi')
        except:
            self.current_lang = 'vi'
    
    def save_language_preference(self):
        """Save language preference to config file"""
        try:
            config = {'language': self.current_lang}
            with open('config.json', 'w', encoding='utf-8') as f:
                json.dump(config, f)
        except:
            pass
    
    def t(self, key):
        """Translate key to current language"""
        return TRANSLATIONS[self.current_lang].get(key, key)
    
    def change_language(self, lang):
        """Change application language - Fast update without recreating widgets"""
        if lang != self.current_lang:
            self.current_lang = lang
            self.save_language_preference()
            # Update all text labels without recreating widgets
            self.update_ui_language()
    
    def update_ui_language(self):
        """Update UI text for current language without recreating widgets"""
        # Update window title
        self.root.title(self.t('app_title'))
        
        # Update header labels
        if 'title_label' in self.widgets:
            self.widgets['title_label'].config(text=self.t('app_title'))
        if 'subtitle_label' in self.widgets:
            self.widgets['subtitle_label'].config(text=self.t('app_subtitle'))
        if 'lang_label' in self.widgets:
            self.widgets['lang_label'].config(text=self.t('language') + ":")
        
        # Update tab names
        if hasattr(self, 'notebook'):
            self.notebook.tab(0, text=self.t('tab_sign'))
            self.notebook.tab(1, text=self.t('tab_cert'))
            self.notebook.tab(2, text=self.t('tab_settings'))
        
        # Update Sign JAR tab
        if 'file_frame' in self.widgets:
            self.widgets['file_frame'].config(text=self.t('select_jar'))
        if 'browse_btn' in self.widgets:
            self.widgets['browse_btn'].config(text=self.t('browse'))
        if 'options_frame' in self.widgets:
            self.widgets['options_frame'].config(text=self.t('options'))
        if 'auto_remove_check' in self.widgets:
            self.widgets['auto_remove_check'].config(text=self.t('auto_remove_sig'))
        if 'auto_jad_check' in self.widgets:
            self.widgets['auto_jad_check'].config(text=self.t('auto_update_jad'))
        if 'sign_btn' in self.widgets:
            self.widgets['sign_btn'].config(text=self.t('sign_jar'))
        if 'remove_btn' in self.widgets:
            self.widgets['remove_btn'].config(text=self.t('remove_sig'))
        if 'verify_btn' in self.widgets:
            self.widgets['verify_btn'].config(text=self.t('verify_sig'))
        if 'log_frame' in self.widgets:
            self.widgets['log_frame'].config(text=self.t('result'))
        
        # Update Certificate tab
        if 'cert_info_frame' in self.widgets:
            self.widgets['cert_info_frame'].config(text=self.t('cert_info'))
        if 'create_cert_btn' in self.widgets:
            self.widgets['create_cert_btn'].config(text=self.t('create_cert'))
        if 'view_cert_btn' in self.widgets:
            self.widgets['view_cert_btn'].config(text=self.t('view_cert'))
        if 'delete_cert_btn' in self.widgets:
            self.widgets['delete_cert_btn'].config(text=self.t('delete_cert'))
        if 'export_cert_btn' in self.widgets:
            self.widgets['export_cert_btn'].config(text=self.t('export_cert'))
        
        # Update Settings tab
        if 'keystore_frame' in self.widgets:
            self.widgets['keystore_frame'].config(text=self.t('keystore_config'))
        if 'cert_details_frame' in self.widgets:
            self.widgets['cert_details_frame'].config(text=self.t('cert_details'))
        if 'save_settings_btn' in self.widgets:
            self.widgets['save_settings_btn'].config(text=self.t('save_settings'))
        if 'about_frame' in self.widgets:
            self.widgets['about_frame'].config(text=self.t('about'))
        if 'about_label' in self.widgets:
            self.widgets['about_label'].config(text=self.t('about_text'))
        
        # Update labels in settings
        for key in ['keystore_label', 'alias_label', 'password_label',
                    'cn_label', 'ou_label', 'o_label', 'l_label', 'c_label']:
            if key in self.widgets:
                label_key = key.replace('_label', '')
                self.widgets[key].config(text=self.t(label_key) + ":")
        
        # Update status bar
        self.status_var.set(self.t('ready'))
    
    def create_widgets(self):
        """Tạo các widget cho giao diện"""
        
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Header
        header_frame = ttk.Frame(self.root, padding="10")
        header_frame.pack(fill=tk.X)
        
        # Title and language selector in same row
        title_lang_frame = ttk.Frame(header_frame)
        title_lang_frame.pack(fill=tk.X)
        
        # Title on left
        title_container = ttk.Frame(title_lang_frame)
        title_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.widgets['title_label'] = ttk.Label(
            title_container,
            text=self.t('app_title'),
            font=("Arial", 16, "bold")
        )
        self.widgets['title_label'].pack()
        
        self.widgets['subtitle_label'] = ttk.Label(
            title_container,
            text=self.t('app_subtitle'),
            font=("Arial", 9)
        )
        self.widgets['subtitle_label'].pack()
        
        # Language selector on right
        lang_frame = ttk.Frame(title_lang_frame)
        lang_frame.pack(side=tk.RIGHT, padx=10)
        
        self.widgets['lang_label'] = ttk.Label(lang_frame, text=self.t('language') + ":")
        self.widgets['lang_label'].pack(side=tk.LEFT, padx=5)
        
        self.lang_var = tk.StringVar(value=self.current_lang)
        lang_combo = ttk.Combobox(
            lang_frame,
            textvariable=self.lang_var,
            values=['vi', 'en'],
            state='readonly',
            width=10
        )
        lang_combo.pack(side=tk.LEFT)
        lang_combo.bind('<<ComboboxSelected>>', lambda e: self.change_language(self.lang_var.get()))
        
        # Display language names
        lang_display = {'vi': '🇻🇳 Tiếng Việt', 'en': '🇬🇧 English'}
        lang_combo.config(values=list(lang_display.values()))
        lang_combo.set(lang_display[self.current_lang])
        
        # Update combobox binding
        def on_lang_change(event):
            selected = lang_combo.get()
            new_lang = 'vi' if '🇻🇳' in selected else 'en'
            self.change_language(new_lang)
        
        lang_combo.bind('<<ComboboxSelected>>', on_lang_change)
        
        # Notebook (Tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Tab 1: Ký JAR
        self.create_sign_tab()
        
        # Tab 2: Quản lý Certificate
        self.create_cert_tab()
        
        # Tab 3: Cài đặt
        self.create_settings_tab()
        
        # Status bar
        self.status_var = tk.StringVar(value=self.t('ready'))
        status_bar = ttk.Label(
            self.root,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        status_bar.pack(fill=tk.X, side=tk.BOTTOM, padx=5, pady=2)
    
    def create_sign_tab(self):
        """Tab ký JAR"""
        sign_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(sign_frame, text=self.t('tab_sign'))
        
        # File selection
        self.widgets['file_frame'] = ttk.LabelFrame(sign_frame, text=self.t('select_jar'), padding="10")
        self.widgets['file_frame'].pack(fill=tk.X, pady=5)
        
        self.jar_path_var = tk.StringVar()
        jar_entry = ttk.Entry(self.widgets['file_frame'], textvariable=self.jar_path_var, width=60)
        jar_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        self.widgets['browse_btn'] = ttk.Button(
            self.widgets['file_frame'],
            text=self.t('browse'),
            command=self.browse_jar
        )
        self.widgets['browse_btn'].pack(side=tk.LEFT)
        
        # Options
        self.widgets['options_frame'] = ttk.LabelFrame(sign_frame, text=self.t('options'), padding="10")
        self.widgets['options_frame'].pack(fill=tk.X, pady=5)
        
        self.auto_remove_sig = tk.BooleanVar(value=True)
        self.widgets['auto_remove_check'] = ttk.Checkbutton(
            self.widgets['options_frame'],
            text=self.t('auto_remove_sig'),
            variable=self.auto_remove_sig
        )
        self.widgets['auto_remove_check'].pack(anchor=tk.W)
        
        self.create_jad = tk.BooleanVar(value=True)
        self.widgets['auto_jad_check'] = ttk.Checkbutton(
            self.widgets['options_frame'],
            text=self.t('auto_update_jad'),
            variable=self.create_jad
        )
        self.widgets['auto_jad_check'].pack(anchor=tk.W)
        
        # Buttons
        btn_frame = ttk.Frame(sign_frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        self.widgets['sign_btn'] = ttk.Button(
            btn_frame,
            text=self.t('sign_jar'),
            command=self.sign_jar,
            width=20
        )
        self.widgets['sign_btn'].pack(side=tk.LEFT, padx=5)
        
        self.widgets['remove_btn'] = ttk.Button(
            btn_frame,
            text=self.t('remove_sig'),
            command=self.remove_signature,
            width=20
        )
        self.widgets['remove_btn'].pack(side=tk.LEFT, padx=5)
        
        self.widgets['verify_btn'] = ttk.Button(
            btn_frame,
            text=self.t('verify_sig'),
            command=self.verify_jar,
            width=20
        )
        self.widgets['verify_btn'].pack(side=tk.LEFT, padx=5)
        
        # Log output
        self.widgets['log_frame'] = ttk.LabelFrame(sign_frame, text=self.t('result'), padding="10")
        self.widgets['log_frame'].pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.sign_log = scrolledtext.ScrolledText(
            self.widgets['log_frame'],
            height=15,
            wrap=tk.WORD,
            font=("Consolas", 9)
        )
        self.sign_log.pack(fill=tk.BOTH, expand=True)
    
    def create_cert_tab(self):
        """Tab quản lý certificate"""
        cert_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(cert_frame, text=self.t('tab_cert'))
        
        # Certificate info
        self.widgets['cert_info_frame'] = ttk.LabelFrame(cert_frame, text=self.t('cert_info'), padding="10")
        self.widgets['cert_info_frame'].pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.cert_info = scrolledtext.ScrolledText(
            self.widgets['cert_info_frame'],
            height=15,
            wrap=tk.WORD,
            font=("Consolas", 9)
        )
        self.cert_info.pack(fill=tk.BOTH, expand=True)
        
        # Buttons
        btn_frame = ttk.Frame(cert_frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        self.widgets['create_cert_btn'] = ttk.Button(
            btn_frame,
            text=self.t('create_cert'),
            command=self.create_certificate,
            width=20
        )
        self.widgets['create_cert_btn'].pack(side=tk.LEFT, padx=5)
        
        self.widgets['view_cert_btn'] = ttk.Button(
            btn_frame,
            text=self.t('view_cert'),
            command=self.view_certificate,
            width=20
        )
        self.widgets['view_cert_btn'].pack(side=tk.LEFT, padx=5)
        
        self.widgets['delete_cert_btn'] = ttk.Button(
            btn_frame,
            text=self.t('delete_cert'),
            command=self.delete_certificate,
            width=20
        )
        self.widgets['delete_cert_btn'].pack(side=tk.LEFT, padx=5)
        
        self.widgets['export_cert_btn'] = ttk.Button(
            btn_frame,
            text=self.t('export_cert'),
            command=self.export_certificate,
            width=20
        )
        self.widgets['export_cert_btn'].pack(side=tk.LEFT, padx=5)
    
    def create_settings_tab(self):
        """Tab cài đặt"""
        settings_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(settings_frame, text=self.t('tab_settings'))
        
        # Keystore settings
        self.widgets["keystore_frame"] = ttk.LabelFrame(settings_frame, text=self.t("keystore_config"), padding="10")
        self.widgets["keystore_frame"].pack(fill=tk.X, pady=5)
        
        # Keystore path
        self.widgets["keystore_label"] = ttk.Label(self.widgets["keystore_frame"], text=self.t("keystore") + ":").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.keystore_var = tk.StringVar(value=self.keystore)
        ttk.Entry(self.widgets["keystore_frame"], textvariable=self.keystore_var, width=50).grid(
            row=0, column=1, sticky=tk.EW, padx=5, pady=5
        )
        
        # Alias
        self.widgets["alias_label"] = ttk.Label(self.widgets["keystore_frame"], text=self.t("alias") + ":").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.alias_var = tk.StringVar(value=self.alias)
        ttk.Entry(self.widgets["keystore_frame"], textvariable=self.alias_var, width=50).grid(
            row=1, column=1, sticky=tk.EW, padx=5, pady=5
        )
        
        # Password
        self.widgets["password_label"] = ttk.Label(self.widgets["keystore_frame"], text=self.t("password") + ":").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.password_var = tk.StringVar(value=self.storepass)
        ttk.Entry(self.widgets["keystore_frame"], textvariable=self.password_var, width=50, show="*").grid(
            row=2, column=1, sticky=tk.EW, padx=5, pady=5
        )
        
        self.widgets["keystore_frame"].columnconfigure(1, weight=1)
        
        # Certificate info
        self.widgets["cert_details_frame"] = ttk.LabelFrame(settings_frame, text=self.t("cert_details"), padding="10")
        self.widgets["cert_details_frame"].pack(fill=tk.X, pady=5)
        
        self.widgets["cn_label"] = ttk.Label(self.widgets["cert_details_frame"], text=self.t("cn") + ":").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.cn_var = tk.StringVar(value="S40 Developer")
        ttk.Entry(self.widgets["cert_details_frame"], textvariable=self.cn_var, width=50).grid(
            row=0, column=1, sticky=tk.EW, padx=5, pady=5
        )
        
        self.widgets["ou_label"] = ttk.Label(self.widgets["cert_details_frame"], text=self.t("ou") + ":").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.ou_var = tk.StringVar(value="Mobile Dev")
        ttk.Entry(self.widgets["cert_details_frame"], textvariable=self.ou_var, width=50).grid(
            row=1, column=1, sticky=tk.EW, padx=5, pady=5
        )
        
        self.widgets["o_label"] = ttk.Label(self.widgets["cert_details_frame"], text=self.t("o") + ":").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.o_var = tk.StringVar(value="MyCompany")
        ttk.Entry(self.widgets["cert_details_frame"], textvariable=self.o_var, width=50).grid(
            row=2, column=1, sticky=tk.EW, padx=5, pady=5
        )
        
        self.widgets["l_label"] = ttk.Label(self.widgets["cert_details_frame"], text=self.t("l") + ":").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.l_var = tk.StringVar(value="Hanoi")
        ttk.Entry(self.widgets["cert_details_frame"], textvariable=self.l_var, width=50).grid(
            row=3, column=1, sticky=tk.EW, padx=5, pady=5
        )
        
        self.widgets["c_label"] = ttk.Label(self.widgets["cert_details_frame"], text=self.t("c") + ":").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.c_var = tk.StringVar(value="VN")
        ttk.Entry(self.widgets["cert_details_frame"], textvariable=self.c_var, width=50).grid(
            row=4, column=1, sticky=tk.EW, padx=5, pady=5
        )
        
        self.widgets["cert_details_frame"].columnconfigure(1, weight=1)
        
        # Save button
        self.widgets['save_settings_btn'] = ttk.Button(
            settings_frame,
            text=self.t('save_settings'),
            command=self.save_settings
        )
        self.widgets['save_settings_btn'].pack(pady=10)
        
        # About
        self.widgets['about_frame'] = ttk.LabelFrame(settings_frame, text=self.t('about'), padding="10")
        self.widgets['about_frame'].pack(fill=tk.X, pady=5)
        
        self.widgets['about_label'] = ttk.Label(
            self.widgets['about_frame'],
            text=self.t('about_text'),
            justify=tk.LEFT
        )
        self.widgets['about_label'].pack()
    
    def check_java(self):
        """Kiểm tra Java JDK"""
        try:
            result = subprocess.run(
                ["java", "-version"],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                self.status_var.set(self.t('java_ready'))
            else:
                self.status_var.set(self.t('java_warning'))
                messagebox.showwarning(
                    self.t('warning'),
                    self.t('java_warning') + "!\nPlease install Java JDK and add to PATH."
                )
        except FileNotFoundError:
            self.status_var.set(self.t('java_error'))
            messagebox.showerror(
                self.t('error'),
                self.t('java_error') + "!\nPlease install Java JDK."
            )
    
    def browse_jar(self):
        """Chọn file JAR"""
        filename = filedialog.askopenfilename(
            title=self.t('select_jar'),
            filetypes=[("JAR files", "*.jar"), ("All files", "*.*")]
        )
        if filename:
            self.jar_path_var.set(filename)
    
    def log_message(self, message, log_widget=None):
        """Ghi log"""
        if log_widget is None:
            log_widget = self.sign_log
        
        log_widget.insert(tk.END, f"[{datetime.now().strftime('%H:%M:%S')}] {message}\n")
        log_widget.see(tk.END)
        self.root.update()
    
    def run_command(self, cmd, log_widget=None):
        """Chạy lệnh và hiển thị output"""
        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            
            for line in process.stdout:
                self.log_message(line.strip(), log_widget)
            
            process.wait()
            return process.returncode == 0
        except Exception as e:
            self.log_message(f"Lỗi: {e}", log_widget)
            return False
    
    def sign_jar(self):
        """Ký file JAR"""
        jar_file = self.jar_path_var.get()
        
        if not jar_file:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn file JAR!")
            return
        
        if not os.path.exists(jar_file):
            messagebox.showerror("Lỗi", f"Không tìm thấy file: {jar_file}")
            return
        
        if not os.path.exists(self.keystore):
            messagebox.showerror(
                "Lỗi",
                "Không tìm thấy keystore!\nVui lòng tạo certificate trước."
            )
            return
        
        self.sign_log.delete(1.0, tk.END)
        self.log_message("Bắt đầu ký file JAR...")
        self.status_var.set("Đang ký JAR...")
        
        def sign_thread():
            try:
                # Kiểm tra chữ ký cũ
                if self.auto_remove_sig.get():
                    self.log_message("Kiểm tra chữ ký cũ...")
                    result = subprocess.run(
                        ["jarsigner", "-verify", jar_file],
                        capture_output=True
                    )
                    
                    if result.returncode == 0:
                        self.log_message("Phát hiện chữ ký cũ. Đang xóa...")
                        if self.remove_signature_internal(jar_file):
                            self.log_message("Đã xóa chữ ký cũ thành công.")
                
                # Tạo tên file output
                jar_path = Path(jar_file)
                signed_jar = jar_path.parent / f"{jar_path.stem}-signed{jar_path.suffix}"
                
                self.log_message(f"Input: {jar_file}")
                self.log_message(f"Output: {signed_jar}")
                
                # Ký JAR
                cmd = [
                    "jarsigner",
                    "-keystore", self.keystore,
                    "-storepass", self.storepass,
                    "-keypass", self.keypass,
                    "-signedjar", str(signed_jar),
                    jar_file,
                    self.alias
                ]
                
                if self.run_command(cmd):
                    self.log_message("=" * 50)
                    self.log_message("Ký JAR thành công!")
                    self.log_message(f"File đã ký: {signed_jar}")
                    self.status_var.set("Ký JAR thành công!")
                    
                    messagebox.showinfo(
                        "Thành công",
                        f"Đã ký JAR thành công!\n\nFile: {signed_jar}"
                    )
                else:
                    self.log_message("Lỗi khi ký JAR!")
                    self.status_var.set("Lỗi khi ký JAR")
                    messagebox.showerror("Lỗi", "Không thể ký file JAR!")
            
            except Exception as e:
                self.log_message(f"Lỗi: {e}")
                self.status_var.set("Lỗi")
                messagebox.showerror("Lỗi", str(e))
        
        threading.Thread(target=sign_thread, daemon=True).start()
    
    def remove_signature_internal(self, jar_file):
        """Xóa chữ ký khỏi JAR (internal)"""
        try:
            temp_jar = jar_file + ".tmp"
            
            with zipfile.ZipFile(jar_file, 'r') as zip_in:
                with zipfile.ZipFile(temp_jar, 'w', zipfile.ZIP_DEFLATED) as zip_out:
                    for item in zip_in.infolist():
                        if item.filename.startswith('META-INF/') and (
                            item.filename.endswith('.SF') or
                            item.filename.endswith('.RSA') or
                            item.filename.endswith('.DSA')
                        ):
                            continue
                        
                        data = zip_in.read(item.filename)
                        zip_out.writestr(item, data)
            
            os.replace(temp_jar, jar_file)
            return True
        except Exception as e:
            self.log_message(f"Lỗi khi xóa chữ ký: {e}")
            if os.path.exists(temp_jar):
                os.remove(temp_jar)
            return False
    
    def remove_signature(self):
        """Xóa chữ ký khỏi JAR"""
        jar_file = self.jar_path_var.get()
        
        if not jar_file:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn file JAR!")
            return
        
        if not os.path.exists(jar_file):
            messagebox.showerror("Lỗi", f"Không tìm thấy file: {jar_file}")
            return
        
        if not messagebox.askyesno(
            "Xác nhận",
            "Bạn có chắc muốn xóa chữ ký khỏi file JAR này?"
        ):
            return
        
        self.sign_log.delete(1.0, tk.END)
        self.log_message("Đang xóa chữ ký...")
        self.status_var.set("Đang xóa chữ ký...")
        
        # Backup
        backup_file = jar_file + ".bak"
        import shutil
        shutil.copy2(jar_file, backup_file)
        self.log_message(f"Đã tạo backup: {backup_file}")
        
        if self.remove_signature_internal(jar_file):
            self.log_message("Đã xóa chữ ký thành công!")
            self.status_var.set("Xóa chữ ký thành công")
            messagebox.showinfo("Thành công", "Đã xóa chữ ký thành công!")
        else:
            self.log_message("Lỗi khi xóa chữ ký!")
            self.status_var.set("Lỗi")
            messagebox.showerror("Lỗi", "Không thể xóa chữ ký!")
    
    def verify_jar(self):
        """Xác minh chữ ký JAR"""
        jar_file = self.jar_path_var.get()
        
        if not jar_file:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn file JAR!")
            return
        
        if not os.path.exists(jar_file):
            messagebox.showerror("Lỗi", f"Không tìm thấy file: {jar_file}")
            return
        
        self.sign_log.delete(1.0, tk.END)
        self.log_message("Đang xác minh chữ ký...")
        self.status_var.set("Đang xác minh...")
        
        cmd = ["jarsigner", "-verify", "-verbose", "-certs", jar_file]
        
        if self.run_command(cmd):
            self.log_message("=" * 50)
            self.log_message("Xác minh thành công!")
            self.status_var.set("Xác minh thành công")
        else:
            self.log_message("Xác minh thất bại!")
            self.status_var.set("Xác minh thất bại")
    
    def create_certificate(self):
        """Tạo certificate mới"""
        if os.path.exists(self.keystore):
            if not messagebox.askyesno(
                "Xác nhận",
                "Keystore đã tồn tại. Bạn có muốn ghi đè?"
            ):
                return
        
        self.cert_info.delete(1.0, tk.END)
        self.log_message("Đang tạo certificate...", self.cert_info)
        self.status_var.set("Đang tạo certificate...")
        
        def create_thread():
            dname = f"CN={self.cn_var.get()}, OU={self.ou_var.get()}, O={self.o_var.get()}, L={self.l_var.get()}, C={self.c_var.get()}"
            
            cmd = [
                "keytool", "-genkeypair",
                "-alias", self.alias,
                "-keyalg", "RSA",
                "-keysize", "2048",
                "-validity", "3650",
                "-keystore", self.keystore,
                "-storepass", self.storepass,
                "-keypass", self.keypass,
                "-dname", dname
            ]
            
            if self.run_command(cmd, self.cert_info):
                self.log_message("=" * 50, self.cert_info)
                self.log_message("Tạo certificate thành công!", self.cert_info)
                self.log_message(f"Keystore: {self.keystore}", self.cert_info)
                self.status_var.set("Tạo certificate thành công")
                messagebox.showinfo("Thành công", "Đã tạo certificate thành công!")
            else:
                self.log_message("Lỗi khi tạo certificate!", self.cert_info)
                self.status_var.set("Lỗi")
                messagebox.showerror("Lỗi", "Không thể tạo certificate!")
        
        threading.Thread(target=create_thread, daemon=True).start()
    
    def view_certificate(self):
        """Xem thông tin certificate"""
        if not os.path.exists(self.keystore):
            messagebox.showerror("Lỗi", "Không tìm thấy keystore!")
            return
        
        self.cert_info.delete(1.0, tk.END)
        self.log_message("Đang đọc thông tin certificate...", self.cert_info)
        self.status_var.set("Đang đọc certificate...")
        
        cmd = [
            "keytool", "-list", "-v",
            "-keystore", self.keystore,
            "-storepass", self.storepass,
            "-alias", self.alias
        ]
        
        if self.run_command(cmd, self.cert_info):
            self.status_var.set("Đã đọc thông tin certificate")
        else:
            self.status_var.set("Lỗi")
    
    def delete_certificate(self):
        """Xóa certificate"""
        if not os.path.exists(self.keystore):
            messagebox.showerror("Lỗi", "Không tìm thấy keystore!")
            return
        
        if not messagebox.askyesno(
            "Xác nhận",
            "Bạn có chắc muốn xóa certificate?"
        ):
            return
        
        self.cert_info.delete(1.0, tk.END)
        self.log_message("Đang xóa certificate...", self.cert_info)
        self.status_var.set("Đang xóa certificate...")
        
        cmd = [
            "keytool", "-delete",
            "-alias", self.alias,
            "-keystore", self.keystore,
            "-storepass", self.storepass
        ]
        
        if self.run_command(cmd, self.cert_info):
            self.log_message("Đã xóa certificate thành công!", self.cert_info)
            self.status_var.set("Xóa certificate thành công")
            messagebox.showinfo("Thành công", "Đã xóa certificate!")
        else:
            self.log_message("Lỗi khi xóa certificate!", self.cert_info)
            self.status_var.set("Lỗi")
            messagebox.showerror("Lỗi", "Không thể xóa certificate!")
    
    def export_certificate(self):
        """Xuất certificate"""
        if not os.path.exists(self.keystore):
            messagebox.showerror("Lỗi", "Không tìm thấy keystore!")
            return
        
        filename = filedialog.asksaveasfilename(
            title="Lưu certificate",
            defaultextension=".cer",
            filetypes=[("Certificate files", "*.cer"), ("All files", "*.*")]
        )
        
        if not filename:
            return
        
        self.cert_info.delete(1.0, tk.END)
        self.log_message("Đang xuất certificate...", self.cert_info)
        self.status_var.set("Đang xuất certificate...")
        
        cmd = [
            "keytool", "-exportcert",
            "-alias", self.alias,
            "-keystore", self.keystore,
            "-storepass", self.storepass,
            "-file", filename
        ]
        
        if self.run_command(cmd, self.cert_info):
            self.log_message(f"Đã xuất certificate: {filename}", self.cert_info)
            self.status_var.set("Xuất certificate thành công")
            messagebox.showinfo("Thành công", f"Đã xuất certificate!\n\n{filename}")
        else:
            self.log_message("Lỗi khi xuất certificate!", self.cert_info)
            self.status_var.set("Lỗi")
            messagebox.showerror("Lỗi", "Không thể xuất certificate!")
    
    def save_settings(self):
        """Lưu cài đặt"""
        self.keystore = self.keystore_var.get()
        self.alias = self.alias_var.get()
        self.storepass = self.password_var.get()
        self.keypass = self.password_var.get()
        
        messagebox.showinfo("Thành công", "Đã lưu cài đặt!")
        self.status_var.set("Đã lưu cài đặt")


def main():
    """Main function"""
    root = tk.Tk()
    app = S40SignApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
