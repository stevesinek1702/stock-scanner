@echo off
REM Script tự động setup dự án cho Windows

echo 📦 Tạo cấu trúc thư mục...

REM Tạo thư mục .github\workflows
mkdir .github\workflows 2>nul

REM Tạo thư mục results
mkdir results 2>nul

echo ✅ Đã tạo xong cấu trúc thư mục!
echo.
echo 📁 Cấu trúc:
echo stock-scanner\
echo ├── .github\
echo │   └── workflows\
echo │       └── scan.yml
echo ├── results\
echo │   └── .gitkeep
echo ├── scanner.py
echo ├── requirements.txt
echo ├── symbols.txt
echo └── README.md
echo.
echo 🚀 Tiếp theo:
echo 1. Copy các file vào đúng vị trí
echo 2. Chạy: git add .
echo 3. Chạy: git commit -m "Initial commit"
echo 4. Chạy: git push

pause
