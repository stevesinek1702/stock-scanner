# 📖 Hướng dẫn Setup chi tiết

## Phương án 1: Upload trực tiếp trên GitHub (KHUYẾN NGHỊ - Đơn giản nhất)

### Bước 1: Tạo repo
1. Vào https://github.com/new
2. Repository name: `stock-scanner`
3. Chọn **Public**
4. ✅ Tích **Add a README file**
5. Click **Create repository**

### Bước 2: Tạo file `.github/workflows/scan.yml`
1. Trong repo, click **Add file** → **Create new file**
2. Ở ô **Name your file**, gõ chính xác: `.github/workflows/scan.yml`
   - Khi gõ dấu `/`, GitHub tự tạo thư mục
   - Gõ tiếp `workflows/` rồi `scan.yml`
3. Copy toàn bộ nội dung file `scan.yml` vào
4. Scroll xuống, click **Commit new file**

### Bước 3: Tạo file `results/.gitkeep`
1. Click **Add file** → **Create new file**
2. Gõ: `results/.gitkeep`
3. Gõ nội dung: `# Folder for scan results`
4. Click **Commit new file**

### Bước 4: Upload các file còn lại
1. Click **Add file** → **Upload files**
2. Kéo thả 4 file:
   - `scanner.py`
   - `requirements.txt`
   - `symbols.txt`
   - `README.md`
3. Click **Commit changes**

### Bước 5: Cấp quyền cho GitHub Actions
1. Vào tab **Settings** (trong repo)
2. Bên trái click **Actions** → **General**
3. Scroll xuống phần **Workflow permissions**
4. Chọn ⚪ **Read and write permissions**
5. Click **Save**

### Bước 6: Bật GitHub Actions
1. Vào tab **Actions**
2. Nếu thấy nút xanh **I understand my workflows, go ahead and enable them**, click vào
3. Xong!

### Bước 7: Chạy thử
1. Vẫn ở tab **Actions**
2. Bên trái click **Stock Scanner**
3. Bên phải click nút **Run workflow**
4. Click **Run workflow** (nút xanh)
5. Đợi 3-5 phút
6. Refresh trang, xem kết quả

### Bước 8: Xem kết quả
1. Vào tab **Code**
2. Click thư mục `results/`
3. Click file `latest.csv`
4. Click nút **Raw** để tải về
5. Mở bằng Excel/Google Sheets

---

## Phương án 2: Dùng Git trên máy tính (Nếu đã cài Git)

### Bước 1: Clone repo
```bash
git clone https://github.com/YOUR_USERNAME/stock-scanner.git
cd stock-scanner
```

### Bước 2: Tạo cấu trúc thư mục

**Trên Windows:**
```cmd
setup.bat
```

**Trên Mac/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

### Bước 3: Copy file vào đúng vị trí
```
stock-scanner/
├── .github/
│   └── workflows/
│       └── scan.yml          ← Copy file scan.yml vào đây
├── results/
│   └── .gitkeep              ← Copy file .gitkeep vào đây
├── scanner.py                ← Copy vào thư mục gốc
├── requirements.txt          ← Copy vào thư mục gốc
├── symbols.txt               ← Copy vào thư mục gốc
└── README.md                 ← Copy vào thư mục gốc
```

### Bước 4: Push lên GitHub
```bash
git add .
git commit -m "Initial commit - Stock Scanner"
git push
```

### Bước 5-8: Giống Phương án 1 (từ bước 5 trở đi)

---

## ✅ Kiểm tra setup thành công

Sau khi setup xong, repo của bạn phải có cấu trúc như sau:

```
stock-scanner/
├── .github/
│   └── workflows/
│       └── scan.yml          ✅
├── results/
│   └── .gitkeep              ✅
├── scanner.py                ✅
├── requirements.txt          ✅
├── symbols.txt               ✅
├── README.md                 ✅
└── (các file khác tùy chọn)
```

Vào repo, bạn phải thấy:
- Thư mục `.github` (có thể ẩn, click "Show hidden files")
- Thư mục `results`
- 4 file: scanner.py, requirements.txt, symbols.txt, README.md

---

## 🐛 Troubleshooting

### Lỗi: "Workflow not found"
**Nguyên nhân:** File `scan.yml` không đúng đường dẫn

**Giải pháp:**
1. Kiểm tra đường dẫn phải là: `.github/workflows/scan.yml`
2. Chú ý dấu chấm `.` ở đầu `.github`
3. Chú ý chữ `s` ở cuối `workflows`

### Lỗi: "Permission denied" khi push
**Giải pháp:**
1. Vào Settings → Actions → General
2. Chọn "Read and write permissions"
3. Save

### Không thấy thư mục `.github`
**Nguyên nhân:** Thư mục ẩn (bắt đầu bằng dấu chấm)

**Giải pháp:**
- Trên GitHub web: Vẫn thấy bình thường
- Trên Windows: Bật "Show hidden files"
- Trên Mac/Linux: Dùng `ls -la` để xem

### Actions không chạy tự động
**Giải pháp:**
1. Kiểm tra tab Actions có bật không
2. Kiểm tra file `scan.yml` có lỗi syntax không
3. Thử chạy thủ công bằng "Run workflow"

---

## 📞 Cần trợ giúp?

Nếu gặp vấn đề:
1. Chụp màn hình lỗi
2. Tạo Issue trên GitHub repo
3. Hoặc liên hệ qua email

---

## 🎉 Chúc mừng!

Nếu setup thành công, tool sẽ tự động chạy mỗi 15 phút và lưu kết quả vào `results/latest.csv`!
