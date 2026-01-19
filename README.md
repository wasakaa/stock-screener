# 📈 Stock Screener - HNX & UPCOM

Web dashboard để phân tích và tìm cơ hội trading trên sàn HNX và UPCOM.

## 🚀 Demo

👉 **https://[YOUR-USERNAME].github.io/stock-screener/stock_screener.html**

## ✨ Tính năng

- 📊 Phân tích 300+ mã cổ phiếu HNX/UPCOM
- 🎯 Tự động tính signal: Uptrend, Reversal, Volume spike
- 🔍 Filter theo sàn, signal type, tìm kiếm mã
- 📱 Responsive design - xem trên mobile OK
- 💯 Score system để đánh giá cơ hội

## 📊 Metrics

- **Price Change**: 10 ngày và 30 ngày
- **Position**: Vị trí giá trong range 90 ngày (0-100%)
- **Volatility**: Biến động giá trung bình
- **Volume Spike**: So sánh với volume trung bình
- **Volume Trend**: Xu hướng volume tăng/giảm

## 🎯 Signal Types

- 🟢 **Near Support + Volume**: Gần đáy với volume tăng
- 🔴 **Near Resistance + Volume**: Gần đỉnh với volume tăng
- 📈 **Strong Uptrend**: Xu hướng tăng mạnh 30 ngày
- 🔄 **Reversal Setup**: Oversold đang đảo chiều
- ⚡ **Positive Momentum**: Động lực tích cực

## 🔄 Cập nhật data

Chạy Python script để generate data mới, sau đó commit file `stocks_data.json`

## ⚠️ Disclaimer

Thông tin chỉ mang tính chất tham khảo. Không phải lời khuyên đầu tư.
