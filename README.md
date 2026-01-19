# 🎯 Stock Screener AI Pro v2.1

**Công cụ phân tích cổ phiếu thông minh với AI 4 tầng + Hệ thống đánh giá thanh khoản**

[![Version](https://img.shields.io/badge/version-2.1.0-blue.svg)](https://github.com/wasakaa/stock-screener)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)](https://wasakaa.github.io/stock-screener)

🌐 **Live Demo**: [https://wasakaa.github.io/stock-screener/stock_screener_v2_liquidity.html](https://wasakaa.github.io/stock-screener/stock_screener_v2_liquidity.html)

---

## 🚀 Version 2.1 - Liquidity System (2026-01-19)

### ✨ Major Update: LIQUIDITY SCORING SYSTEM

**Giải quyết vấn đề quan trọng:** *"Mua được nhưng không bán được = MẮC KẸT VỐN"*

Phiên bản 2.1 bổ sung hệ thống đánh giá thanh khoản toàn diện, giúp trader tránh rủi ro mắc kẹt vốn khi giao dịch các mã có thanh khoản thấp.

---

## 📊 Thống kê hệ thống

- **654 mã cổ phiếu** từ 3 sàn (HNX, UPCOM, HOSE)
- **496 mã an toàn** (thanh khoản ≥6/10) - 75.8%
- **206 mã xuất sắc** (thanh khoản 8-10/10) - 31.5%
- **AI đã override 3 mã** nguy hiểm (thanh khoản quá thấp)

---

## 🆕 Tính năng mới v2.1

### 1. 💧 Liquidity Scoring System (0-10)

Đánh giá thanh khoản dựa trên 4 yếu tố:

- **Average Volume (40%)**: Khối lượng giao dịch trung bình
- **Volume Consistency (30%)**: Độ ổn định của volume
- **Volatility/Spread (20%)**: Biến động giá (proxy cho bid-ask spread)
- **Days to Exit (10%)**: Thời gian ước tính để thoát lệnh

#### Phân loại thanh khoản:

| Score | Level | Đánh giá | Exit Time | Max Capital | Trade Safety |
|-------|-------|----------|-----------|-------------|--------------|
| 8-10 | 🟢 **XUẤT SẮC** | Rất dễ giao dịch | 1-2 ngày | Không giới hạn | ✅ Rất an toàn |
| 6-8 | 🟡 **TỐT** | Dễ vào/ra lệnh | 3-5 ngày | 50-100 triệu | ✅ An toàn |
| 4-6 | 🟠 **TRUNG BÌNH** | Cần cẩn thận | 5-10 ngày | 20-30 triệu | ⚠️ Trade nhỏ |
| 2-4 | 🔴 **YẾU** | Rủi ro cao | 10-20 ngày | 10-20 triệu | ⚠️ Chỉ long-term |
| 0-2 | ⛔ **RẤT YẾU** | Rất nguy hiểm | 20+ ngày | ❌ Không nên | ❌ TRÁNH |

### 2. 🤖 Smart AI Override

AI tự động điều chỉnh khuyến nghị dựa trên thanh khoản:

- **Liquidity < 4**: AI override "MUA" → "GIỮ" + cảnh báo
- **Liquidity < 6**: Force "DÀI HẠN" (không cho swing trading)
- Hiển thị warning rõ ràng cho mã rủi ro

### 3. 📊 Risk Management Tools

- **Exit Time Estimates**: Biết trước bao lâu có thể thoát lệnh
- **Max Capital Suggestions**: Gợi ý vốn tối đa an toàn
- **Warning System**: Cảnh báo real-time cho từng mã
- **Trading Style Adjustment**: Tự động điều chỉnh phong cách giao dịch

### 4. 🔍 Enhanced Filters

- Filter "Chỉ mã an toàn (≥6)"
- Filter theo liquidity level (Xuất sắc, Tốt, Trung bình)
- Visual badges với màu sắc trực quan
- Statistics breakdown by liquidity

---

## 🎯 Tính năng chính (Core Features)

### 🤖 AI 4 Tầng

1. **Level 1 - Rule-based Analysis**
   - RSI (Relative Strength Index)
   - MACD (Moving Average Convergence Divergence)
   - MA20/MA50 (Moving Averages)
   - Volume spike detection
   - Momentum indicators

2. **Level 2 - Pattern Recognition**
   - Bullish/Bearish divergences
   - Candlestick patterns
   - Support/Resistance levels

3. **Level 3 - ML Prediction**
   - Predicted price change (5 days)
   - Confidence scores
   - Trend forecasting

4. **Level 4 - Ensemble AI**
   - Kết hợp 3 tầng trên
   - Composite scoring (0-10)
   - Final recommendation với confidence

### 📈 Trading Style Analysis

- **Lướt sóng (SWING)**: Phù hợp cho giao dịch 3-10 ngày
- **Dài hạn (LONG-TERM)**: Phù hợp cho nắm giữ 1-3 tháng
- Tự động phân loại dựa trên volatility + liquidity

### 📊 Technical Indicators

- RSI với oversold/overbought zones
- MACD với signal line
- MA20 & MA50
- Volume analysis
- Price range (90 days)
- Volatility metrics

### 🎨 User Interface

- **Responsive design**: Desktop, tablet, mobile
- **Real-time filters**: 9 bộ lọc kết hợp
- **Interactive charts**: Modal với thông tin chi tiết
- **Visual badges**: Liquidity, Exchange, AI recommendations
- **Dark/Light theme**: Gradient background

---

## 📊 Impact: Before vs After v2.1

| Aspect | Before v2.1 | After v2.1 |
|--------|-------------|------------|
| **Liquidity Awareness** | ❌ Không biết mã nào khó bán | ✅ Liquidity score cho tất cả |
| **AI Recommendations** | ❌ Recommend cả mã rủi ro | ✅ Tự động override mã nguy hiểm |
| **Risk Assessment** | ❌ User tự đánh giá | ✅ Warning system tự động |
| **Exit Planning** | ❌ Không có thông tin | ✅ Exit time + Max capital |
| **Capital Management** | ❌ Không có gợi ý | ✅ Suggestions theo liquidity |
| **Trading Style** | ⚠️ Manual selection | ✅ Auto-adjust by liquidity |

### Kết quả:

- ✅ **496 mã an toàn** để trade (75.8%)
- ✅ **158 mã cảnh báo** rõ ràng
- ✅ **3 mã bị AI override** tự động
- ✅ **KHÔNG CÒN RỦI RO MẮC KẸT VỐN** 🎉

---

## 🚀 Cách sử dụng

### 1. Truy cập Web App

Mở trình duyệt và truy cập: [Stock Screener AI Pro](https://wasakaa.github.io/stock-screener/stock_screener_ai_pro.html)

### 2. Sử dụng Filters

- **Sàn**: HNX, UPCOM, HOSE
- **Thanh khoản**: Chọn mức an toàn (≥6) hoặc theo level
- **AI Khuyến nghị**: MUA MẠNH, MUA, GIỮ
- **Phong cách**: Lướt sóng, Dài hạn
- **Tìm kiếm**: Nhập mã cổ phiếu

### 3. Xem Chi Tiết

Click vào card hoặc nút "Xem biểu đồ & chi tiết" để thấy:
- Liquidity score và risk level
- AI analysis 4 tầng
- Technical indicators
- Entry/Target/Stop-loss zones
- Exit time và max capital

### 4. Đọc Warnings

⚠️ **Chú ý các cảnh báo:**
- "⚠️ Volume không ổn định"
- "⚠️ Exit time dài"
- "❌ KHÔNG NÊN TRADE"
- "💀 Nguy cơ mắc kẹt vốn cao"

---

## 🔄 Cập nhật dữ liệu

### Option 1: Python Local

```bash
# 1. Chuẩn bị CSV files
# Đặt files trong cùng folder với script:
#   - CafeF.HNX.Upto[DATE].csv
#   - CafeF.UPCOM.Upto[DATE].csv
#   - CafeF.HOSE.Upto[DATE].csv

# 2. Chạy script
python update_data.py

# 3. Upload JSON mới lên GitHub
git add stocks_data_ai_complete.json
git commit -m "Update data: [DATE]"
git push
```

### Option 2: Google Colab

```bash
# 1. Upload CSV files lên Google Drive
#    Folder: /MyDrive/stock-screener-data/

# 2. Mở Stock_Screener_Update.ipynb trong Colab

# 3. Run All Cells

# 4. Download stocks_data_ai_complete.json

# 5. Upload lên GitHub
```

Xem chi tiết: [UPDATE_GUIDE.md](UPDATE_GUIDE.md)

---

## 📁 Cấu trúc dự án

```
stock-screener/
├── stock_screener_ai_pro.html      # Web UI v2.1
├── stocks_data_ai_complete.json    # Data with liquidity (6.6 MB)
├── update_data.py                  # Python script v2.1
├── Stock_Screener_Update.ipynb     # Colab notebook (3 sàn)
├── README.md                       # Documentation
├── UPDATE_GUIDE.md                 # Update instructions
├── UPDATE_NOTES_v2.1.md           # Version 2.1 changelog
├── DEPLOYMENT_PLAN_v2.1.md        # Deployment guide
└── COLAB_UPDATE_GUIDE.md          # Colab-specific guide
```

---

## 🔧 Technical Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Data Processing**: Python 3.8+
  - pandas (data manipulation)
  - numpy (numerical computing)
  - json (data serialization)
- **Hosting**: GitHub Pages
- **Version Control**: Git
- **Environment**: Local Python / Google Colab

---

## 📖 Documentation

- **[UPDATE_GUIDE.md](UPDATE_GUIDE.md)**: Hướng dẫn cập nhật dữ liệu
- **[UPDATE_NOTES_v2.1.md](UPDATE_NOTES_v2.1.md)**: Chi tiết thay đổi v2.1
- **[DEPLOYMENT_PLAN_v2.1.md](DEPLOYMENT_PLAN_v2.1.md)**: Hướng dẫn deploy
- **[COLAB_UPDATE_GUIDE.md](COLAB_UPDATE_GUIDE.md)**: Hướng dẫn Colab

---

## ⚠️ Disclaimer

**Thông tin chỉ mang tính tham khảo, không phải lời khuyên đầu tư.**

- Dữ liệu từ CafeF.vn (90 ngày gần nhất)
- AI predictions không đảm bảo chính xác 100%
- Luôn thực hiện phân tích riêng trước khi đầu tư
- Quản lý rủi ro và vốn cẩn thận
- **Đặc biệt chú ý liquidity warnings** để tránh mắc kẹt vốn

---

## 🤝 Contributing

Mọi đóng góp đều được hoan nghênh! Nếu bạn có ý tưởng cải tiến:

1. Fork repo
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📝 Changelog

### v2.1.0 (2026-01-19)

#### ✨ New Features:
- **Liquidity Scoring System** (0-10) for all stocks
- **AI Override** for low liquidity stocks (<4)
- **Exit Time Estimates** based on volume analysis
- **Max Capital Recommendations** by liquidity level
- **Enhanced Filters** with liquidity options
- **Warning System** for high-risk stocks
- **Trading Style Auto-adjustment** based on liquidity

#### 🔧 Improvements:
- 3 exchanges support: HNX + UPCOM + HOSE
- Increased coverage: 654 stocks (from 283)
- Better risk management tools
- Enhanced UI with liquidity badges
- Mobile responsive improvements

#### 📊 Statistics:
- Safe stocks (≥6): 496 (75.8%)
- Excellent liquidity (8-10): 206 (31.5%)
- AI overridden: 3 stocks

#### 🐛 Bug Fixes:
- Fixed volume spike calculation edge cases
- Improved RSI accuracy for low-volume stocks
- Better handling of missing data

### v2.0.0 (2026-01-16)
- AI 4-layer system
- Trading style analysis
- HNX + UPCOM support

### v1.0.0 (2026-01-14)
- Initial release
- Basic technical indicators
- HNX only

---

## 📧 Contact

- GitHub: [@wasakaa](https://github.com/wasakaa)
- Issues: [GitHub Issues](https://github.com/wasakaa/stock-screener/issues)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Data source: [CafeF.vn](https://cafef.vn)
- Inspired by: Trading community feedback
- Special thanks: All contributors and users

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=wasakaa/stock-screener&type=Date)](https://star-history.com/#wasakaa/stock-screener&Date)

---

<div align="center">

**Made with ❤️ for Vietnamese traders**

⭐ Star this repo if you find it helpful!

[🚀 Try it now](https://wasakaa.github.io/stock-screener/stock_screener_ai_pro.html) | [📖 Documentation](UPDATE_GUIDE.md) | [🐛 Report Bug](https://github.com/wasakaa/stock-screener/issues)

</div>
