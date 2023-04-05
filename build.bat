@echo off
python -m pip install --upgrade -r requirements.txt
pyinstaller ./src/__init__.spec
