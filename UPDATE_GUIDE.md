# 📖 HƯỚNG DẪN UPDATE DỮ LIỆU

## 🔄 Khi nào cần update?

- **Hàng tuần**: Update data mới từ CafeF
- **Sau sự kiện lớn**: Thị trường biến động mạnh
- **Theo lịch riêng**: Tùy nhu cầu của bạn

---

## 📥 Bước 1: Download CSV mới từ CafeF

### Cách download:

1. Truy cập **CafeF.vn** hoặc nguồn data khác
2. Export data theo format:
   - `CafeF.HNX.Upto[NGAY.THANG.NAM].csv`
   - `CafeF.UPCOM.Upto[NGAY.THANG.NAM].csv`

**Ví dụ:**
```
CafeF.HNX.Upto21.01.2026.csv
CafeF.UPCOM.Upto21.01.2026.csv
```

3. Lưu vào folder project (cùng folder với `update_data.py`)

---

## 🐍 Bước 2: Chạy Python script

### Option A: Dùng script tự động (RECOMMENDED)

```bash
# Đảm bảo có Python 3.8+
python --version

# Install dependencies (lần đầu tiên)
pip install pandas numpy

# Chạy update script
python update_data.py
```

**Output:**
```
🚀 STOCK SCREENER AI - DATA UPDATE
======================================================================
📂 Step 1: Loading CSV files...
   ✓ Found: CafeF.HNX.Upto21.01.2026.csv
   ✓ Found: CafeF.UPCOM.Upto21.01.2026.csv
   ✓ HNX: 13,500 rows
   ✓ UPCOM: 23,000 rows

📊 Step 2: Processing data (90 days)...
   ✓ Filtered to 90 days: 13,189 + 22,738 rows

📈 Step 3: Calculating technical indicators...
      HNX: 50/299...
      HNX: 100/299...
      ...
   ✓ Processed: 283 liquid stocks

🤖 Step 4: Running AI analysis (4 levels)...
   ✓ AI analysis completed

💾 Step 5: Saving data...
   ✓ stocks_data_ai_complete.json (2.9 MB)

======================================================================
✅ UPDATE HOÀN THÀNH!
======================================================================
📊 Tổng: 283 mã
📅 Data: 2026-01-21
💾 Size: 2.9 MB

🚀 Tiếp theo:
   1. Upload stocks_data_ai_complete.json lên GitHub
   2. Web tự động cập nhật!
```

### Option B: Manual (nếu không có Python)

1. Dùng service trực tuyến (Google Colab, Repl.it)
2. Upload CSV files
3. Chạy code
4. Download JSON output

---

## 📤 Bước 3: Upload lên GitHub

### Cách 1: GitHub Web Interface

1. Vào repo: `https://github.com/wasakaa/stock-screener`
2. Click vào file `stocks_data_ai_complete.json`
3. Click nút **Pencil** (Edit)
4. Delete nội dung cũ
5. Copy-paste nội dung JSON mới
6. Scroll xuống → **Commit changes**
7. Message: "Update data: [NGÀY THÁNG]"
8. Click **Commit**

### Cách 2: Git Command Line

```bash
# Trong folder project
git add stocks_data_ai_complete.json
git commit -m "Update data: 21/01/2026"
git push origin main
```

---

## ✅ Bước 4: Verify Update

1. Đợi **2-3 phút** để GitHub xử lý
2. Truy cập: `https://wasakaa.github.io/stock-screener/stock_screener_ai_pro.html`
3. Check **"Cập nhật:"** date ở header
4. Test click vào vài mã → Xem chart có đúng không

**Nếu chưa cập nhật:**
- Hard refresh: `Ctrl + Shift + R` (Windows) / `Cmd + Shift + R` (Mac)
- Clear cache browser
- Đợi thêm 5 phút

---

## 🔧 Troubleshooting

### Lỗi: "No module named 'pandas'"

```bash
pip install pandas numpy
```

### Lỗi: "FileNotFoundError: CafeF.HNX"

- Đảm bảo CSV files cùng folder với `update_data.py`
- Kiểm tra tên file đúng format: `CafeF.HNX.Upto[DATE].csv`

### Lỗi: "MemoryError" (RAM không đủ)

- Giảm số ngày: Sửa `90` thành `60` trong script
- Hoặc dùng máy có RAM lớn hơn

### JSON quá lớn (>25MB)

GitHub có limit 25MB/file. Nếu vượt:
- Giảm số ngày data (60 thay vì 90)
- Hoặc dùng GitHub LFS
- Hoặc host JSON ở nơi khác (Google Drive, AWS S3)

### Web không load data

1. Check console (F12 → Console tab)
2. Xem có lỗi CORS không?
3. Đảm bảo JSON valid: https://jsonlint.com/

---

## 📊 Tùy chỉnh AI

### Thay đổi liquidity filter

Trong `update_data.py`, dòng:
```python
stocks = [s for s in all_stocks if 
          (s['exchange'] == 'HNX' and s['avg_volume'] > 10000) or 
          (s['exchange'] == 'UPCOM' and s['avg_volume'] > 5000)]
```

**Giảm để có nhiều mã hơn:**
```python
stocks = [s for s in all_stocks if 
          (s['exchange'] == 'HNX' and s['avg_volume'] > 5000) or 
          (s['exchange'] == 'UPCOM' and s['avg_volume'] > 2000)]
```

### Thay đổi AI scoring

Trong `Level 1 Analysis`, sửa weights:
```python
if stock['rsi'] < 30:
    score += 4  # Tăng từ 3 → 4 để RSI quan trọng hơn
```

---

## ⏱️ Automation (Advanced)

### Setup cron job (Linux/Mac)

```bash
# Edit crontab
crontab -e

# Chạy mỗi Chủ nhật 10PM
0 22 * * 0 cd /path/to/project && python update_data.py && git add . && git commit -m "Auto update" && git push
```

### Setup GitHub Actions (Auto deploy)

Tạo `.github/workflows/update.yml`:
```yaml
name: Update Data
on:
  schedule:
    - cron: '0 22 * * 0'  # Every Sunday 10PM
  workflow_dispatch:
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install pandas numpy
      - run: python update_data.py
      - run: |
          git config user.name github-actions
          git config user.email github-actions@github.com
          git add .
          git commit -m "Auto update data"
          git push
```

---

## 🎯 Best Practices

✅ **Update đều đặn**: Mỗi tuần hoặc 2 tuần/lần  
✅ **Backup**: Lưu JSON cũ trước khi update  
✅ **Test local**: Mở HTML local trước khi push  
✅ **Git message rõ ràng**: "Update data: 21/01/2026 - 283 stocks"  
✅ **Monitor errors**: Check console logs sau update  

---

## 📞 Support

Nếu gặp vấn đề:
1. Check [Troubleshooting](#troubleshooting) section
2. Open GitHub Issue
3. Contact: [@wasakaa](https://github.com/wasakaa)

---

**Happy Trading! 📈🚀**
