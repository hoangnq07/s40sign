#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for S40 Sign Tool
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='s40-sign-tool',
    version='1.1.1',
    description='Certificate and signing tool for Nokia S40 Java applications',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='S40 Sign Tool Team',
    author_email='support@example.com',
    url='https://github.com/yourusername/SignS40',
    license='MIT',
    
    py_modules=['s40_sign_app', 'sign_tool'],
    
    install_requires=[
        # Tkinter is included in Python standard library
    ],
    
    extras_require={
        'dev': [
            'pyinstaller>=5.0',
            'flake8>=4.0',
            'pylint>=2.0',
        ],
    },
    
    entry_points={
        'console_scripts': [
            's40-sign=sign_tool:main',
        ],
        'gui_scripts': [
            's40-sign-gui=s40_sign_app:main',
        ],
    },
    
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Environment :: X11 Applications',
        'Environment :: Win32 (MS Windows)',
        'Environment :: MacOS X',
    ],
    
    keywords='s40 nokia java signing certificate jar jad mobile',
    
    python_requires='>=3.6',
    
    project_urls={
        'Bug Reports': 'https://github.com/yourusername/SignS40/issues',
        'Source': 'https://github.com/yourusername/SignS40',
        'Documentation': 'https://github.com/yourusername/SignS40/blob/master/README.md',
    },
)
