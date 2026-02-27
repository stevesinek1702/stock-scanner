# 📊 Stock Scanner - MA100/MA200

Tool tự động quét cổ phiếu Việt Nam tìm tín hiệu kỹ thuật dựa trên MA100 và MA200.

## 🎯 Tính năng

1. **Gần MA100/MA200**: Tìm cổ phiếu có giá ±1% so với MA100 hoặc MA200
2. **Cắt lên MA100/MA200**: Tìm cổ phiếu vừa cắt lên (golden cross) MA100 hoặc MA200

## 🚀 Hướng dẫn Setup

### Bước 1: Tạo GitHub Repository

1. Vào https://github.com/new
2. Đặt tên repo: `stock-scanner` (hoặc tên bạn thích)
3. Chọn **Public** (để dùng GitHub Actions miễn phí)
4. Tích ✅ **Add a README file**
5. Click **Create repository**

### Bước 2: Upload code lên GitHub

**Cách 1: Dùng GitHub Web UI (đơn giản nhất)**

1. Vào repo vừa tạo
2. Click **Add file** → **Upload files**
3. Kéo thả tất cả file:
   - `scanner.py`
   - `requirements.txt`
   - `symbols.txt`
   - `.github/workflows/scan.yml` (tạo thư mục `.github/workflows/` trước)
4. Click **Commit changes**

**Cách 2: Dùng Git (nếu quen)**

```bash
git clone https://github.com/YOUR_USERNAME/stock-scanner.git
cd stock-scanner

# Copy tất cả file vào đây
# Sau đó:
git add .
git commit -m "Initial commit"
git push
```

### Bước 3: Bật GitHub Actions

1. Vào repo → tab **Actions**
2. Click **I understand my workflows, go ahead and enable them**
3. Xong! GitHub sẽ tự động chạy mỗi 15 phút

### Bước 4: Chạy thử ngay

1. Vào tab **Actions**
2. Click workflow **Stock Scanner** bên trái
3. Click **Run workflow** → **Run workflow**
4. Đợi 3-5 phút, xem kết quả

## 📁 Kết quả

Sau khi chạy, kết quả được lưu tại:
- `results/latest.csv` - File CSV
- `results/latest.json` - File JSON

Xem kết quả:
1. Vào repo → thư mục `results/`
2. Click file `latest.csv` → Click **Raw** để tải về
3. Mở bằng Excel/Google Sheets

## ⚙️ Tùy chỉnh

### Thay đổi tần suất chạy

Sửa file `.github/workflows/scan.yml`:

```yaml
schedule:
  - cron: '*/15 * * * *'  # Mỗi 15 phút
  # - cron: '0 * * * *'   # Mỗi giờ
  # - cron: '0 9 * * *'   # 9h sáng mỗi ngày
```

### Thêm/bớt mã cổ phiếu

Sửa file `symbols.txt`, mỗi dòng 1 mã.

### Thay đổi ngưỡng gần MA

Sửa file `scanner.py`, dòng 67:

```python
near_ma100 = check_near_ma(latest_close, latest_ma100, 0.01)  # 0.01 = 1%
# Đổi thành 0.02 nếu muốn ±2%
```

## 📊 Ví dụ kết quả

| Symbol | Close | MA100 | MA200 | Diff_MA100_% | Near_MA100 | Cross_MA100 | Signals |
|--------|-------|-------|-------|--------------|------------|-------------|---------|
| FPT    | 135.5 | 134.2 | 128.3 | +0.97        | ✓          |             | Gần MA100 |
| VNM    | 78.2  | 75.1  | 76.8  | +4.13        |            | ✓           | Cắt lên MA100 |

## 🔧 Chạy local (test)

```bash
# Cài Python 3.11+
pip install -r requirements.txt
python scanner.py
```

## 📝 Lưu ý

- GitHub Actions free: 2000 phút/tháng
- Chạy mỗi 15 phút, mỗi lần ~2 phút → ~2880 phút/tháng
- Nếu vượt quota, đổi sang chạy mỗi giờ hoặc mỗi ngày

## 🆘 Troubleshooting

**Lỗi: "Workflow not found"**
- Kiểm tra file `.github/workflows/scan.yml` có đúng đường dẫn không

**Lỗi: "Permission denied"**
- Vào repo → Settings → Actions → General
- Scroll xuống **Workflow permissions**
- Chọn **Read and write permissions**
- Click **Save**

**Không có kết quả**
- Vào Actions → Click vào run mới nhất → Xem logs
- Kiểm tra API FireAnt có hoạt động không

## 📧 Liên hệ

Có vấn đề? Tạo Issue trên GitHub repo này.
