# 📖 Stock Screener AI Pro - Hướng dẫn cập nhật dữ liệu

**Version: 2.1.0 | Updated: 2026-01-19**

---

## 📋 Tổng quan

Hướng dẫn này giúp bạn cập nhật dữ liệu cổ phiếu cho Stock Screener AI Pro v2.1, bao gồm:

- ✅ Liquidity scoring system
- ✅ 3 sàn: HNX, UPCOM, HOSE
- ✅ AI 4-layer analysis
- ✅ Technical indicators

---

## 🎯 Mục tiêu

Sau khi hoàn thành, bạn sẽ có:
- File `stocks_data_ai_complete.json` mới với liquidity scores
- Data từ 3 sàn (HNX + UPCOM + HOSE)
- ~500-600 mã cổ phiếu được phân tích
- Web app tự động cập nhật

---

## 🔄 Tần suất cập nhật

**Khuyến nghị**: Cập nhật **mỗi tuần 1 lần** (thứ 2 hoặc thứ 6)

- Dữ liệu CafeF thường cập nhật cuối ngày giao dịch
- Script phân tích 90 ngày gần nhất
- GitHub Pages rebuild trong 2-3 phút

---

## 📥 Bước 1: Download dữ liệu CSV

### Option 1: CafeF.vn (Manual)

1. Truy cập: https://s.cafef.vn/screener.aspx
2. Chọn sàn (HNX / UPCOM / HOSE)
3. Export → Download CSV
4. Lặp lại cho cả 3 sàn

**Files cần có:**
```
CafeF.HNX.Upto[DATE].csv
CafeF.UPCOM.Upto[DATE].csv
CafeF.HOSE.Upto[DATE].csv
```

### Option 2: API (Advanced)

Nếu có script tự động download, đảm bảo format CSV giống CafeF.

---

## 🐍 Bước 2: Chạy script Python

### Method A: Python Local (Recommended)

#### Yêu cầu:
- Python 3.8+
- pandas, numpy

#### Cài đặt:

```bash
# Nếu chưa có Python, download tại python.org

# Cài đặt thư viện
pip install pandas numpy
```

#### Chạy script:

```bash
# 1. Đặt CSV files và update_data.py trong cùng folder

# 2. Chạy script
python update_data.py

# 3. Đợi 2-3 phút

# 4. Kiểm tra output
ls -lh stocks_data_ai_complete.json
```

#### Output mong đợi:

```
🚀 STOCK SCREENER AI v2.1 - WITH LIQUIDITY SYSTEM
======================================================================

📂 Step 1: Loading CSV files (3 exchanges)...
   ✓ HNX: CafeF.HNX.Upto14.01.2026.csv
      Rows: 13,189
   ✓ UPCOM: CafeF.UPCOM.Upto14.01.2026.csv
      Rows: 22,738
   ✓ HOSE: CafeF.HOSE.Upto16.01.2026.csv
      Rows: 25,456

📊 Step 2: Processing data (90 days)...
   ✓ HNX: 1,234 rows
   ✓ UPCOM: 2,567 rows
   ✓ HOSE: 3,890 rows

📈 Step 3: Calculating technical indicators...
   ✓ HNX: 120 stocks processed
   ✓ UPCOM: 163 stocks processed
   ✓ HOSE: 371 stocks processed

💧 Step 4: Calculating liquidity scores...
   ✓ Liquidity breakdown:
      🟢 Excellent (8-10): 206
      🟡 Good (6-8): 290
      🟠 Moderate (4-6): 148
      🔴 Poor (2-4): 10
      ⛔ Very Poor (<2): 0

🤖 Step 5: Running AI analysis (4 levels)...
   ✓ AI analysis completed

💾 Step 6: Saving data...
   ✓ stocks_data_ai_complete.json (6.6 MB)

======================================================================
✅ UPDATE HOÀN THÀNH v2.1!
======================================================================

📊 Tổng quan:
   • Version: 2.1
   • Tổng: 654 mã
   • Sàn: HNX, UPCOM, HOSE
   • HNX: 120 mã (98 mã an toàn)
   • UPCOM: 163 mã (135 mã an toàn)
   • HOSE: 371 mã (263 mã an toàn)

💧 Liquidity:
   • 496 mã trade an toàn (liquidity ≥6)
   • 158 mã cẩn thận (liquidity <6)
   • 3 mã bị AI override do liquidity

📅 Data: 2026-01-16
💾 Size: 6.6 MB

🎯 TOP 3 SAFE PICKS (High Liquidity + AI Recommend):

1. VNM (HOSE) - 🟢🟢 MUA MẠNH
   💯 AI Score: 9.2/10
   💧 Liquidity: 🟢 XUẤT SẮC (9.5/10)
   📊 Volume: 2,500,000 | Exit: 1 ngày
   💰 Max Capital: Không giới hạn

2. HPG (HOSE) - 🟢 MUA
   💯 AI Score: 8.5/10
   💧 Liquidity: 🟢 XUẤT SẮC (9.1/10)
   📊 Volume: 1,800,000 | Exit: 1-2 ngày
   💰 Max Capital: Không giới hạn

3. CEO (HNX) - 🟢 MUA
   💯 AI Score: 7.8/10
   💧 Liquidity: 🟡 TỐT (7.2/10)
   📊 Volume: 45,000 | Exit: 3-5 ngày
   💰 Max Capital: 50-100 triệu

======================================================================
🚀 LIQUIDITY SYSTEM ACTIVE!
======================================================================
```

---

### Method B: Google Colab (No Python installation needed)

#### Bước 1: Chuẩn bị Google Drive

```
1. Truy cập: drive.google.com
2. Tạo folder: stock-screener-data
3. Upload 3 CSV files vào folder
```

#### Bước 2: Mở Colab Notebook

```
1. Truy cập: colab.research.google.com
2. File → Upload notebook
3. Upload: Stock_Screener_Update.ipynb
```

#### Bước 3: Chạy notebook

```python
# Cell 1: Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')
# → Click "Connect to Google Drive" → Authorize

# Cell 2: Config
FOLDER_PATH = '/content/drive/MyDrive/stock-screener-data'
import os
os.chdir(FOLDER_PATH)

# Cell 3: Main Script
# (Copy toàn bộ code từ update_data.py)
# → Runtime → Run All

# Cell 4: Download
from google.colab import files
files.download('stocks_data_ai_complete.json')
```

#### Bước 4: Download JSON

File sẽ tự động download về máy (thường vào folder Downloads)

---

## 📤 Bước 3: Upload lên GitHub

### Option 1: GitHub Web Interface

```
1. Vào GitHub repo của bạn
2. Click vào file: stocks_data_ai_complete.json
3. Click icon ✏️ (Edit)
4. Delete all content
5. Paste nội dung JSON mới
6. Scroll xuống → Commit changes
   Message: "Update data: 2026-01-16"
7. Click "Commit changes"
```

### Option 2: Git Command Line

```bash
# 1. Copy JSON file vào repo folder
cp stocks_data_ai_complete.json /path/to/your/repo/

# 2. Git commands
cd /path/to/your/repo
git add stocks_data_ai_complete.json
git commit -m "Update data: 2026-01-16 - 654 stocks with liquidity"
git push origin main
```

### Option 3: GitHub Desktop

```
1. Mở GitHub Desktop
2. Select repository
3. Copy JSON file vào repo folder
4. GitHub Desktop tự động detect changes
5. Commit message: "Update data: 2026-01-16"
6. Click "Commit to main"
7. Click "Push origin"
```

---

## ✅ Bước 4: Verify

### 4.1. Đợi GitHub Pages rebuild

- Thời gian: 2-3 phút
- Check tại: Settings → Pages → Build status

### 4.2. Test live site

```
1. Truy cập: https://wasakaa.github.io/stock-screener/stock_screener_ai_pro.html
2. Refresh (Ctrl+F5)
3. Check "Cập nhật:" date → phải là ngày mới
4. Check "Tổng số mã" → phải đúng số lượng
5. Test filters → hoạt động OK
6. Click vào 1 mã → check liquidity badge
```

### 4.3. Checklist

✅ Stats cards hiển thị đúng  
✅ "Cập nhật:" date mới  
✅ Tổng số mã đúng  
✅ Liquidity badges hiển thị  
✅ Filters hoạt động  
✅ Modal chart OK  
✅ Mobile responsive  

---

## 🐛 Troubleshooting

### Lỗi: "No CSV files found"

**Nguyên nhân**: Script không tìm thấy CSV files

**Giải pháp**:
```bash
# Check files có đúng folder không
ls *.csv

# Check tên files đúng format
# Đúng: CafeF.HNX.Upto14.01.2026.csv
# Sai: hnx_data.csv
```

### Lỗi: "KeyError: '<DTYYYYMMDD>'"

**Nguyên nhân**: CSV format không đúng

**Giải pháp**:
- Re-download từ CafeF.vn
- Không chỉnh sửa CSV bằng Excel
- Đảm bảo encoding UTF-8

### Lỗi: "FileNotFoundError: stocks_data_ai_complete.json"

**Nguyên nhân**: Script chạy thành công nhưng không tìm thấy output

**Giải pháp**:
```bash
# Check current directory
pwd

# Tìm file
find . -name "stocks_data_ai_complete.json"
```

### Lỗi: Web hiển thị "Đang tải dữ liệu..." mãi

**Nguyên nhân**: JSON file lỗi hoặc không load được

**Giải pháp**:
1. Check console (F12) → có error gì không
2. Verify JSON syntax: https://jsonlint.com
3. Check file size: phải ~6-7 MB
4. Clear browser cache (Ctrl+Shift+Del)

### Warning: "⚠️ pandas FutureWarning"

**Không sao!** Chỉ là warning, không ảnh hưởng kết quả.

---

## 💡 Tips & Best Practices

### 1. Backup trước khi update

```bash
# Backup JSON cũ
cp stocks_data_ai_complete.json stocks_data_backup_$(date +%Y%m%d).json
```

### 2. Verify data quality

```python
# Quick check
import json

with open('stocks_data_ai_complete.json') as f:
    data = json.load(f)

print(f"Version: {data['version']}")
print(f"Total stocks: {data['total_stocks']}")
print(f"Exchanges: {data['exchanges']}")
print(f"Safe stocks: {data['statistics']['safe_to_trade']}")
```

### 3. Tự động hóa (Advanced)

Tạo cron job để tự động chạy hàng tuần:

```bash
# Linux/Mac: crontab -e
0 9 * * 1 cd /path/to/script && python update_data.py && git add . && git commit -m "Auto update" && git push
```

### 4. Monitor file size

JSON file không nên vượt quá 10 MB (GitHub limit: 100 MB, nhưng nên giữ nhỏ để load nhanh)

### 5. Version control

Mỗi lần update, nên note lại:
- Date
- Number of stocks
- Any issues encountered

---

## 📊 Hiểu output JSON

### Structure:

```json
{
  "last_update": "2026-01-16",
  "version": "2.1",
  "total_stocks": 654,
  "exchanges": ["HNX", "UPCOM", "HOSE"],
  "liquidity_levels": {
    "excellent": 206,
    "good": 290,
    "moderate": 148,
    "poor": 10,
    "very_poor": 0
  },
  "statistics": {
    "swing_trading": 137,
    "long_term": 517,
    "strong_buy": 45,
    "buy": 123,
    "liquidity_overridden": 3,
    "safe_to_trade": 496
  },
  "stocks": [
    {
      "ticker": "VNM",
      "exchange": "HOSE",
      "price": 85.5,
      "liquidity": {
        "score": 9.5,
        "level": "EXCELLENT",
        "label": "🟢 XUẤT SẮC",
        "trade_safe": true,
        "max_capital": "Không giới hạn",
        "exit_time": "1-2 ngày"
      },
      "ai_ensemble": {
        "final_action": "STRONG_BUY",
        "final_label": "🟢🟢 MUA MẠNH",
        "composite_score": 9.2,
        "confidence": 85
      }
    }
  ]
}
```

---

## 📖 Tài liệu liên quan

- **[README.md](README.md)**: Tổng quan dự án
- **[UPDATE_NOTES_v2.1.md](UPDATE_NOTES_v2.1.md)**: Chi tiết thay đổi v2.1
- **[COLAB_UPDATE_GUIDE.md](COLAB_UPDATE_GUIDE.md)**: Hướng dẫn Colab chi tiết
- **[DEPLOYMENT_PLAN_v2.1.md](DEPLOYMENT_PLAN_v2.1.md)**: Deployment guide

---

## 🆘 Support

Nếu gặp vấn đề:

1. **Check Troubleshooting section** ở trên
2. **Open GitHub Issue**: [Create Issue](https://github.com/wasakaa/stock-screener/issues)
3. **Include**:
   - Error message đầy đủ
   - Python version (`python --version`)
   - OS (Windows/Mac/Linux)
   - Steps to reproduce

---

## ✨ Advanced: Thêm sàn mới

Nếu muốn thêm sàn khác (VD: HSX):

1. Download CSV với format giống CafeF
2. Update `update_data.py`:
   ```python
   # Thêm vào line ~55
   hsx_files = [f for f in csv_files if 'HSX' in f]

   # Thêm vào line ~75
   if hsx_files:
       hsx_file = sorted(hsx_files)[-1]
       dfs['HSX'] = pd.read_csv(hsx_file)

   # Thêm liquidity threshold trong calculate_liquidity_score()
   ```

---

<div align="center">

**Happy Trading! 📈**

[🏠 Back to README](README.md) | [🐛 Report Issue](https://github.com/wasakaa/stock-screener/issues)

</div>
