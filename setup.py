# -*- coding: utf-8 -*-
"""
    cookieclicker_autoclicker
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Setup script for packaging and installing cookieclicker_autoclicker
"""
import pathlib
from setuptools import setup, find_packages

this_directory = pathlib.Path(__file__).parent.resolve()
long_description = (this_directory / 'README.md').read_text(encoding='utf-8')

setup(
    name="cookieclicker_autoclicker",
    version="1.0.0",
    description=("Automatically keeps clicking on cookie clicker and golden cookies"),
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Hugo Cisneiros (Eitch)',
    author_email='eitch@naovouler.com.br',
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='macro, gui, cookieclicker, automation, cheating',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.11, <4",
    install_requires=[
        "pyautogui==0.9.54",
        "opencv-python==4.10.0.84",
        "pillow==10.4.0"
    ],
    entry_points={
        'console_scripts': [
            'cookieclicker_autoclicker=cookieclicker_autoclicker.cli:main',
        ],
    },
)
