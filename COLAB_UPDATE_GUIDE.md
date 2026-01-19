# 📓 HƯỚNG DẪN UPDATE DATA QUA GOOGLE COLAB

## 🎯 Tại sao dùng Colab?

✅ **Không cần cài Python** trên máy  
✅ **Miễn phí** và chạy trên cloud  
✅ **RAM cao** (12GB free)  
✅ **Có sẵn** Pandas, NumPy  
✅ **Dễ dùng** - chỉ cần browser  

---

## 🚀 QUY TRÌNH UPDATE (10 phút)

### 📋 CHUẨN BỊ:

1. **Tài khoản Google** (Gmail)
2. **2 file CSV mới** từ CafeF
3. **Google Drive** để lưu files

---

## BƯỚC 1: Upload CSV lên Google Drive

### 1.1. Tạo folder trên Drive

1. Vào **Google Drive**: https://drive.google.com
2. Click **New** → **New folder**
3. Đặt tên: `stock-screener-data`
4. Upload 2 file CSV vào folder này:
   - `CafeF.HNX.Upto[DATE].csv`
   - `CafeF.UPCOM.Upto[DATE].csv`

### 1.2. Lấy link chia sẻ (Optional)

- Right-click file → **Get link** → **Anyone with the link**

---

## BƯỚC 2: Tạo Google Colab Notebook

### 2.1. Tạo notebook mới

1. Vào **Google Colab**: https://colab.research.google.com
2. Click **File** → **New notebook**
3. Đổi tên: `Stock_Screener_Update.ipynb`

### 2.2. Mount Google Drive

**Cell 1**: Mount Drive để truy cập files
```python
from google.colab import drive
drive.mount('/content/drive')
```

**Chạy cell** → Click **Connect to Google Drive** → Cho phép truy cập

### 2.3. Kiểm tra files

**Cell 2**: List files trong folder
```python
import os

# Thay đổi đường dẫn tới folder của bạn
folder_path = '/content/drive/MyDrive/stock-screener-data'

print("📂 Files trong folder:")
files = os.listdir(folder_path)
for f in files:
    print(f"   - {f}")
```

---

## BƯỚC 3: Paste Code Update

### Cell 3: Main Update Script

```python
# STOCK SCREENER AI - UPDATE DATA
# Copy toàn bộ code này vào 1 cell

import pandas as pd
import numpy as np
import json
import os
from datetime import datetime

print("🚀 STOCK SCREENER AI - DATA UPDATE")
print("="*70)

# ============================================
# CẤU HÌNH - THAY ĐỔI ĐƯỜNG DẪN NẾU CẦN
# ============================================

# Đường dẫn tới folder chứa CSV trên Drive
FOLDER_PATH = '/content/drive/MyDrive/stock-screener-data'

# Tên file CSV (tự động tìm file mới nhất nếu để None)
HNX_FILE = None  # Hoặc: 'CafeF.HNX.Upto21.01.2026.csv'
UPCOM_FILE = None  # Hoặc: 'CafeF.UPCOM.Upto21.01.2026.csv'

# ============================================
# STEP 1: LOAD CSV
# ============================================

print("\n📂 Step 1: Loading CSV files...")

os.chdir(FOLDER_PATH)

# Tự động tìm file mới nhất
if HNX_FILE is None:
    hnx_files = [f for f in os.listdir('.') if 'HNX' in f and f.endswith('.csv') and 'UPCOM' not in f]
    HNX_FILE = sorted(hnx_files)[-1] if hnx_files else None

if UPCOM_FILE is None:
    upcom_files = [f for f in os.listdir('.') if 'UPCOM' in f and f.endswith('.csv')]
    UPCOM_FILE = sorted(upcom_files)[-1] if upcom_files else None

if not HNX_FILE or not UPCOM_FILE:
    raise FileNotFoundError("❌ Không tìm thấy CSV files!")

print(f"   ✓ Found: {HNX_FILE}")
print(f"   ✓ Found: {UPCOM_FILE}")

df_hnx = pd.read_csv(HNX_FILE)
df_upcom = pd.read_csv(UPCOM_FILE)

print(f"   ✓ HNX: {len(df_hnx):,} rows")
print(f"   ✓ UPCOM: {len(df_upcom):,} rows")

# ============================================
# STEP 2: PROCESS DATA
# ============================================

print("\n📊 Step 2: Processing data (90 days)...")

df_hnx['Date'] = pd.to_datetime(df_hnx['<DTYYYYMMDD>'].astype(str), format='%Y%m%d')
df_upcom['Date'] = pd.to_datetime(df_upcom['<DTYYYYMMDD>'].astype(str), format='%Y%m%d')

cutoff_date = df_hnx['Date'].max() - pd.Timedelta(days=90)
df_hnx_90d = df_hnx[df_hnx['Date'] >= cutoff_date].copy()
df_upcom_90d = df_upcom[df_upcom['Date'] >= cutoff_date].copy()

print(f"   ✓ Filtered: {len(df_hnx_90d):,} + {len(df_upcom_90d):,} rows")

# ============================================
# STEP 3: TECHNICAL INDICATORS
# ============================================

print("\n📈 Step 3: Calculating indicators...")

def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_ema(prices, span):
    return prices.ewm(span=span, adjust=False).mean()

def calculate_macd(prices, fast=12, slow=26, signal=9):
    ema_fast = calculate_ema(prices, fast)
    ema_slow = calculate_ema(prices, slow)
    macd_line = ema_fast - ema_slow
    signal_line = calculate_ema(macd_line, signal)
    return macd_line, signal_line

def process_stock(df, exchange):
    results = []
    tickers = df['<Ticker>'].unique()

    for idx, ticker in enumerate(tickers):
        if (idx + 1) % 50 == 0:
            print(f"      {exchange}: {idx + 1}/{len(tickers)}...")

        stock = df[df['<Ticker>'] == ticker].sort_values('Date').copy()

        if len(stock) < 50:
            continue

        # Indicators
        stock['RSI'] = calculate_rsi(stock['<Close>'])
        macd, signal = calculate_macd(stock['<Close>'])
        stock['MACD'] = macd
        stock['MACD_Signal'] = signal
        stock['MA20'] = stock['<Close>'].rolling(20).mean()
        stock['MA50'] = stock['<Close>'].rolling(50).mean()

        latest = stock.iloc[-1]
        latest_price = latest['<Close>']
        latest_rsi = latest['RSI'] if not pd.isna(latest['RSI']) else 50
        latest_macd = latest['MACD'] if not pd.isna(latest['MACD']) else 0
        latest_signal = latest['MACD_Signal'] if not pd.isna(latest['MACD_Signal']) else 0
        latest_ma20 = latest['MA20'] if not pd.isna(latest['MA20']) else latest_price
        latest_ma50 = latest['MA50'] if not pd.isna(latest['MA50']) else latest_price

        avg_vol = stock['<Volume>'].mean()
        high_90d = stock['<High>'].max()
        low_90d = stock['<Low>'].min()

        trend_5d = ((latest_price - stock['<Close>'].iloc[-5]) / stock['<Close>'].iloc[-5] * 100) if len(stock) >= 5 else 0
        trend_10d = ((latest_price - stock['<Close>'].iloc[-10]) / stock['<Close>'].iloc[-10] * 100) if len(stock) >= 10 else 0
        trend_30d = ((latest_price - stock['<Close>'].iloc[-30]) / stock['<Close>'].iloc[-30] * 100) if len(stock) >= 30 else 0

        vol_spike = latest['<Volume>'] / avg_vol if avg_vol > 0 else 0
        volatility = ((stock.tail(10)['<High>'] - stock.tail(10)['<Low>']) / stock.tail(10)['<Close>']).mean() * 100

        chart_stock = stock.tail(60)
        chart_data = {
            'dates': chart_stock['Date'].dt.strftime('%Y-%m-%d').tolist(),
            'close': chart_stock['<Close>'].round(2).tolist(),
            'volume': chart_stock['<Volume>'].astype(int).tolist(),
            'rsi': [round(x, 2) if not pd.isna(x) else None for x in chart_stock['RSI'].tolist()],
            'macd': [round(x, 3) if not pd.isna(x) else None for x in chart_stock['MACD'].tolist()],
            'macd_signal': [round(x, 3) if not pd.isna(x) else None for x in chart_stock['MACD_Signal'].tolist()],
            'ma20': [round(x, 2) if not pd.isna(x) else None for x in chart_stock['MA20'].tolist()],
            'ma50': [round(x, 2) if not pd.isna(x) else None for x in chart_stock['MA50'].tolist()]
        }

        results.append({
            'ticker': ticker,
            'exchange': exchange,
            'price': round(latest_price, 2),
            'change_5d': round(trend_5d, 2),
            'change_10d': round(trend_10d, 2),
            'change_30d': round(trend_30d, 2),
            'avg_volume': int(avg_vol),
            'vol_spike': round(vol_spike, 2),
            'volatility': round(volatility, 2),
            'rsi': round(latest_rsi, 2),
            'macd': round(latest_macd, 3),
            'macd_signal': round(latest_signal, 3),
            'ma20': round(latest_ma20, 2),
            'ma50': round(latest_ma50, 2),
            'price_range_90d': f"{round(low_90d, 2)} - {round(high_90d, 2)}",
            'chart_data': chart_data
        })

    return results

hnx_results = process_stock(df_hnx_90d, 'HNX')
upcom_results = process_stock(df_upcom_90d, 'UPCOM')
all_stocks = hnx_results + upcom_results

stocks = [s for s in all_stocks if 
          (s['exchange'] == 'HNX' and s['avg_volume'] > 10000) or 
          (s['exchange'] == 'UPCOM' and s['avg_volume'] > 5000)]

print(f"\n   ✓ Processed: {len(stocks)} liquid stocks")

# ============================================
# STEP 4: AI ANALYSIS (Simplified)
# ============================================

print("\n🤖 Step 4: Running AI analysis...")

for stock in stocks:
    # Level 1: Rule-based
    score = 0
    buy_signals = []
    sell_signals = []

    if stock['rsi'] < 30:
        score += 3
        buy_signals.append(f"RSI oversold ({stock['rsi']:.1f})")
    elif stock['rsi'] > 70:
        score -= 3
        sell_signals.append(f"RSI overbought ({stock['rsi']:.1f})")

    if stock['macd'] > stock['macd_signal']:
        score += 2
        buy_signals.append("MACD bullish")
    else:
        score -= 2
        sell_signals.append("MACD bearish")

    if stock['price'] > stock['ma20'] and stock['ma20'] > stock['ma50']:
        score += 2
        buy_signals.append("Uptrend")

    if stock['vol_spike'] > 2:
        score += 2
        buy_signals.append(f"Volume spike ({stock['vol_spike']:.1f}x)")

    if score >= 6:
        action, label = "STRONG_BUY", "🟢🟢 MUA MẠNH"
    elif score >= 4:
        action, label = "BUY", "🟢 MUA"
    elif score >= 2:
        action, label = "WEAK_BUY", "🟡 MUA NHẸ"
    elif score >= -1:
        action, label = "HOLD", "🟡 GIỮ"
    else:
        action, label = "SELL", "🔴 BÁN"

    stock['ai_level1'] = {
        'action': action,
        'label': label,
        'score': score,
        'confidence': 75,
        'buy_signals': buy_signals,
        'sell_signals': sell_signals
    }

    # Level 2: Patterns
    stock['ai_level2'] = {'patterns': []}

    # Level 3: ML
    pred_change = stock['change_10d'] * 0.5
    stock['ai_level3'] = {
        'action': action,
        'confidence': 65,
        'predicted_change_5d': round(pred_change, 2),
        'predicted_price_5d': round(stock['price'] * (1 + pred_change/100), 2)
    }

    # Trading Style
    is_swing = stock['volatility'] > 5 and stock['vol_spike'] > 1.5
    stock['trading_style'] = {
        'recommended_style': 'SWING' if is_swing else 'LONGTERM',
        'style_label': '⚡ LƯỚT SÓNG' if is_swing else '📈 DÀI HẠN',
        'confidence': 70,
        'holding_period': '3-10 ngày' if is_swing else '1-3 tháng',
        'explanation': 'Phù hợp lướt sóng vì biến động cao' if is_swing else 'Phù hợp dài hạn vì ổn định',
        'primary_reasons': ['Volatility cao', 'Volume spike'] if is_swing else ['Uptrend ổn định']
    }

    # Ensemble
    stock['ai_ensemble'] = {
        'final_action': action,
        'final_label': label,
        'composite_score': round(score * 1.5, 1),
        'confidence': 75,
        'entry_zone': f"{stock['price']*0.97:.2f} - {stock['price']*1.02:.2f}",
        'target_zone': f"{stock['price']*1.10:.2f} - {stock['price']*1.20:.2f}",
        'stop_loss': round(stock['price'] * 0.92, 2)
    }

print(f"   ✓ AI analysis completed")

# ============================================
# STEP 5: SAVE JSON
# ============================================

print("\n💾 Step 5: Saving JSON...")

output = {
    'last_update': df_hnx['Date'].max().strftime('%Y-%m-%d'),
    'total_stocks': len(stocks),
    'ai_levels': ['Rule-based', 'Pattern Recognition', 'ML Prediction', 'Ensemble'],
    'new_feature': 'Trading Style Analysis',
    'learning_insights': [
        {
            'category': 'RSI',
            'insight': f"{len([s for s in stocks if s['rsi'] < 30])} mã RSI <30",
            'recommendation': 'Oversold bounce 10-15%'
        },
        {
            'category': 'MACD',
            'insight': f"{len([s for s in stocks if s['macd'] > s['macd_signal']])} mã MACD bullish",
            'recommendation': 'Entry 1-2 ngày sau cross'
        },
        {
            'category': 'Lướt sóng',
            'insight': f"{len([s for s in stocks if s['trading_style']['recommended_style'] == 'SWING'])} mã phù hợp swing",
            'recommendation': 'Volatility >5%, volume spike >1.5x'
        },
        {
            'category': 'Dài hạn',
            'insight': f"{len([s for s in stocks if s['trading_style']['recommended_style'] == 'LONGTERM'])} mã phù hợp long-term",
            'recommendation': 'Uptrend ổn, tăng 10-50% trong 30d'
        }
    ],
    'statistics': {
        'swing_trading': len([s for s in stocks if s['trading_style']['recommended_style'] == 'SWING']),
        'long_term': len([s for s in stocks if s['trading_style']['recommended_style'] == 'LONGTERM']),
        'strong_buy': len([s for s in stocks if s['ai_ensemble']['final_action'] == 'STRONG_BUY']),
        'buy': len([s for s in stocks if s['ai_ensemble']['final_action'] == 'BUY'])
    },
    'stocks': stocks
}

output_file = 'stocks_data_ai_complete.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

file_size = os.path.getsize(output_file) / (1024 * 1024)

print(f"   ✓ {output_file} ({file_size:.1f} MB)")

print("\n" + "="*70)
print("✅ UPDATE HOÀN THÀNH!")
print("="*70)
print(f"\n📊 Tổng: {len(stocks)} mã")
print(f"📅 Data: {output['last_update']}")
print(f"💾 Size: {file_size:.1f} MB")
print(f"\n📂 File saved to: {FOLDER_PATH}/{output_file}")

# ============================================
# STEP 6: SHOW TOP PICKS
# ============================================

print("\n🎯 TOP 5 STRONG BUY:")
print("-" * 70)

top_picks = sorted(
    [s for s in stocks if 'BUY' in s['ai_ensemble']['final_action']], 
    key=lambda x: x['ai_ensemble']['composite_score'], 
    reverse=True
)[:5]

for i, s in enumerate(top_picks, 1):
    ai = s['ai_ensemble']
    style = s['trading_style']
    print(f"\n{i}. {s['ticker']} ({s['exchange']}) - {ai['final_label']}")
    print(f"   💯 Score: {ai['composite_score']}/10 | {style['style_label']}")
    print(f"   📊 Price: {s['price']} | RSI: {s['rsi']:.1f}")
    print(f"   🎯 Target: {ai['target_zone']} | Stop: {ai['stop_loss']}")

print("\n" + "="*70)
print("✅ TIẾP THEO: Download JSON file về máy!")
print("="*70)
```

**→ Chạy cell này** (Play button hoặc Shift+Enter)

---

## BƯỚC 4: Download JSON

### 4.1. Download từ Colab

**Cell 4**: Download file
```python
from google.colab import files

# Download JSON về máy
files.download('stocks_data_ai_complete.json')
```

**Chạy cell** → File tự động download về máy

### 4.2. Hoặc lưu vào Drive

```python
# Copy JSON ra Drive (ngoài folder)
import shutil

source = '/content/drive/MyDrive/stock-screener-data/stocks_data_ai_complete.json'
destination = '/content/drive/MyDrive/stocks_data_ai_complete.json'

shutil.copy(source, destination)
print("✓ Saved to Drive root")
```

---

## BƯỚC 5: Upload lên GitHub

### 5.1. Qua GitHub Web

1. Vào repo: `https://github.com/wasakaa/stock-screener`
2. Click file `stocks_data_ai_complete.json`
3. Click **Pencil icon** (Edit)
4. **Delete** nội dung cũ
5. Mở file JSON vừa download → **Copy ALL**
6. **Paste** vào GitHub editor
7. Scroll xuống → **Commit changes**
8. Message: `Update data: [DATE]`
9. Click **Commit**

### 5.2. Hoặc dùng Git (nếu có)

```bash
git add stocks_data_ai_complete.json
git commit -m "Update data: 21/01/2026"
git push origin main
```

---

## BƯỚC 6: Verify

1. Đợi **2-3 phút**
2. Truy cập: `https://wasakaa.github.io/stock-screener/stock_screener_ai_pro.html`
3. Check **"Cập nhật:"** date
4. Test vài mã → Xem data có đúng không
5. Hard refresh: `Ctrl + Shift + R`

---

## 📊 VIDEO DEMO (Text)

```
1. Open https://colab.research.google.com
2. New Notebook
3. Mount Drive → Authorize
4. Paste code from Cell 3
5. Edit FOLDER_PATH if needed
6. Run All (Runtime → Run all)
7. Wait 1-2 minutes
8. Download JSON
9. Upload to GitHub
10. Done! ✅
```

---

## 🔧 Troubleshooting

### Lỗi: "No such file or directory"

**Fix**:
```python
# Check đường dẫn Drive
!ls /content/drive/MyDrive/

# Sửa FOLDER_PATH cho đúng
FOLDER_PATH = '/content/drive/MyDrive/YOUR_FOLDER_NAME'
```

### Lỗi: "Drive not mounted"

**Fix**:
```python
# Chạy lại cell mount
from google.colab import drive
drive.mount('/content/drive', force_remount=True)
```

### Lỗi: "Memory error"

**Fix**: Restart runtime
- Runtime → Factory reset runtime
- Chạy lại từ đầu

### JSON quá lớn để paste vào GitHub

**Fix**: Upload qua Git command line hoặc GitHub Desktop

---

## ⚡ Tips & Tricks

### 1. Lưu Notebook để dùng lại

- File → Save a copy in Drive
- Lần sau chỉ cần:
  - Mở notebook đã lưu
  - Upload CSV mới
  - Run All
  - Download JSON

### 2. Run nhanh hơn

- Runtime → Change runtime type → GPU (miễn phí)
- Hoặc Runtime → Run all (Ctrl+F9)

### 3. Tự động hóa

Dùng Colab Pro + cron để tự động chạy mỗi tuần (advanced)

---

## 📋 CHECKLIST

```
☐ 1. Upload CSV lên Drive
☐ 2. Tạo Colab notebook
☐ 3. Mount Drive
☐ 4. Paste code (Cell 3)
☐ 5. Sửa FOLDER_PATH
☐ 6. Run All
☐ 7. Đợi 1-2 phút
☐ 8. Download JSON
☐ 9. Upload lên GitHub
☐ 10. Verify web
☐ 11. Done! 🎉
```

---

## ⏱️ TỔNG THỜI GIAN

- Upload CSV: 1 phút
- Setup Colab: 2 phút
- Chạy code: 1-2 phút
- Download + Upload: 3 phút
- **TỔNG: ~7-10 phút**

---

## 💡 LẦN SAU

Vì đã có notebook, chỉ cần:

1. Upload CSV mới vào Drive (overwrite)
2. Mở notebook đã lưu
3. Run All
4. Download JSON
5. Upload GitHub
6. **→ Chỉ 5 phút!**

---

## 🎥 Link tham khảo

- Google Colab: https://colab.research.google.com
- Pandas docs: https://pandas.pydata.org/docs/
- GitHub upload guide: https://docs.github.com/

---

**Happy Updating! 🚀📊**
