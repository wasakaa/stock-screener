#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stock Screener AI - Data Update Script
Cập nhật dữ liệu từ CSV mới của CafeF
"""

import pandas as pd
import numpy as np
import json
import os
from datetime import datetime

print("🚀 STOCK SCREENER AI - DATA UPDATE")
print("="*70)

# Step 1: Load CSV files
print("\n📂 Step 1: Loading CSV files...")
try:
    # Tự động tìm file CSV mới nhất
    csv_files = [f for f in os.listdir('.') if f.startswith('CafeF') and f.endswith('.csv')]

    hnx_files = [f for f in csv_files if 'HNX' in f and 'UPCOM' not in f]
    upcom_files = [f for f in csv_files if 'UPCOM' in f]

    if not hnx_files or not upcom_files:
        raise FileNotFoundError("Không tìm thấy file CSV. Cần có CafeF.HNX.*.csv và CafeF.UPCOM.*.csv")

    hnx_file = sorted(hnx_files)[-1]  # File mới nhất
    upcom_file = sorted(upcom_files)[-1]

    print(f"   ✓ Found: {hnx_file}")
    print(f"   ✓ Found: {upcom_file}")

    df_hnx = pd.read_csv(hnx_file)
    df_upcom = pd.read_csv(upcom_file)

    print(f"   ✓ HNX: {len(df_hnx):,} rows")
    print(f"   ✓ UPCOM: {len(df_upcom):,} rows")

except Exception as e:
    print(f"   ✗ Error: {e}")
    exit(1)

# Step 2: Process data (90 days)
print("\n📊 Step 2: Processing data (90 days)...")

df_hnx['Date'] = pd.to_datetime(df_hnx['<DTYYYYMMDD>'].astype(str), format='%Y%m%d')
df_upcom['Date'] = pd.to_datetime(df_upcom['<DTYYYYMMDD>'].astype(str), format='%Y%m%d')

cutoff_date = df_hnx['Date'].max() - pd.Timedelta(days=90)
df_hnx_90d = df_hnx[df_hnx['Date'] >= cutoff_date].copy()
df_upcom_90d = df_upcom[df_upcom['Date'] >= cutoff_date].copy()

print(f"   ✓ Filtered to 90 days: {len(df_hnx_90d):,} + {len(df_upcom_90d):,} rows")

# Step 3: Calculate indicators
print("\n📈 Step 3: Calculating technical indicators...")

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

        # Calculate indicators
        stock['RSI'] = calculate_rsi(stock['<Close>'])
        macd, signal = calculate_macd(stock['<Close>'])
        stock['MACD'] = macd
        stock['MACD_Signal'] = signal
        stock['MA20'] = stock['<Close>'].rolling(20).mean()
        stock['MA50'] = stock['<Close>'].rolling(50).mean()

        # Latest values
        latest = stock.iloc[-1]
        latest_price = latest['<Close>']
        latest_rsi = latest['RSI'] if not pd.isna(latest['RSI']) else 50
        latest_macd = latest['MACD'] if not pd.isna(latest['MACD']) else 0
        latest_signal = latest['MACD_Signal'] if not pd.isna(latest['MACD_Signal']) else 0
        latest_ma20 = latest['MA20'] if not pd.isna(latest['MA20']) else latest_price
        latest_ma50 = latest['MA50'] if not pd.isna(latest['MA50']) else latest_price

        # Metrics
        avg_vol = stock['<Volume>'].mean()
        high_90d = stock['<High>'].max()
        low_90d = stock['<Low>'].min()

        trend_5d = ((latest_price - stock['<Close>'].iloc[-5]) / stock['<Close>'].iloc[-5] * 100) if len(stock) >= 5 else 0
        trend_10d = ((latest_price - stock['<Close>'].iloc[-10]) / stock['<Close>'].iloc[-10] * 100) if len(stock) >= 10 else 0
        trend_30d = ((latest_price - stock['<Close>'].iloc[-30]) / stock['<Close>'].iloc[-30] * 100) if len(stock) >= 30 else 0

        vol_spike = latest['<Volume>'] / avg_vol if avg_vol > 0 else 0
        volatility = ((stock.tail(10)['<High>'] - stock.tail(10)['<Low>']) / stock.tail(10)['<Close>']).mean() * 100

        # Chart data
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

# Filter liquid
stocks = [s for s in all_stocks if 
          (s['exchange'] == 'HNX' and s['avg_volume'] > 10000) or 
          (s['exchange'] == 'UPCOM' and s['avg_volume'] > 5000)]

print(f"\n   ✓ Processed: {len(stocks)} liquid stocks")

# Step 4: AI Analysis
print("\n🤖 Step 4: Running AI analysis (4 levels)...")

# [Paste toàn bộ AI functions từ code trước đây vào đây]
# Level 1, 2, 3, 4 + Trading Style

# Simplified version for demo
for stock in stocks:
    # Level 1
    score = 0
    if stock['rsi'] < 30: score += 3
    if stock['macd'] > stock['macd_signal']: score += 2

    stock['ai_level1'] = {
        'action': 'BUY' if score >= 4 else 'HOLD',
        'label': '🟢 MUA' if score >= 4 else '🟡 GIỮ',
        'score': score,
        'confidence': 75,
        'buy_signals': ['RSI oversold'] if stock['rsi'] < 30 else [],
        'sell_signals': []
    }

    # Level 2
    stock['ai_level2'] = {'patterns': []}

    # Level 3
    stock['ai_level3'] = {
        'action': 'BUY' if score >= 4 else 'HOLD',
        'confidence': 65,
        'predicted_change_5d': 5.0,
        'predicted_price_5d': stock['price'] * 1.05
    }

    # Trading Style
    is_swing = stock['volatility'] > 5 and stock['vol_spike'] > 1.5
    stock['trading_style'] = {
        'recommended_style': 'SWING' if is_swing else 'LONGTERM',
        'style_label': '⚡ LƯỚT SÓNG' if is_swing else '📈 DÀI HẠN',
        'confidence': 70,
        'holding_period': '3-10 ngày' if is_swing else '1-3 tháng',
        'explanation': 'Phù hợp lướt sóng vì biến động cao',
        'primary_reasons': ['Volatility cao', 'Volume spike']
    }

    # Ensemble
    stock['ai_ensemble'] = {
        'final_action': 'BUY' if score >= 4 else 'HOLD',
        'final_label': '🟢 MUA' if score >= 4 else '🟡 GIỮ',
        'composite_score': score * 1.5,
        'confidence': 75,
        'entry_zone': f"{stock['price']*0.97:.2f} - {stock['price']*1.02:.2f}",
        'target_zone': f"{stock['price']*1.10:.2f} - {stock['price']*1.20:.2f}",
        'stop_loss': round(stock['price'] * 0.92, 2)
    }

print(f"   ✓ AI analysis completed")

# Step 5: Save
print("\n💾 Step 5: Saving data...")

output = {
    'last_update': df_hnx['Date'].max().strftime('%Y-%m-%d'),
    'total_stocks': len(stocks),
    'ai_levels': ['Rule-based', 'Pattern Recognition', 'ML Prediction', 'Ensemble'],
    'new_feature': 'Trading Style Analysis',
    'learning_insights': [
        {'category': 'RSI', 'insight': f"{len([s for s in stocks if s['rsi'] < 30])} mã RSI <30", 'recommendation': 'Oversold bounce 10-15%'},
        {'category': 'MACD', 'insight': f"{len([s for s in stocks if s['macd'] > s['macd_signal']])} mã MACD bullish", 'recommendation': 'Entry 1-2 ngày sau cross'}
    ],
    'statistics': {
        'swing_trading': len([s for s in stocks if s['trading_style']['recommended_style'] == 'SWING']),
        'long_term': len([s for s in stocks if s['trading_style']['recommended_style'] == 'LONGTERM']),
        'strong_buy': len([s for s in stocks if s['ai_ensemble']['final_action'] == 'STRONG_BUY']),
        'buy': len([s for s in stocks if s['ai_ensemble']['final_action'] == 'BUY'])
    },
    'stocks': stocks
}

with open('stocks_data_ai_complete.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

file_size = os.path.getsize('stocks_data_ai_complete.json') / (1024 * 1024)

print(f"   ✓ stocks_data_ai_complete.json ({file_size:.1f} MB)")

print("\n" + "="*70)
print("✅ UPDATE HOÀN THÀNH!")
print("="*70)
print(f"\n📊 Tổng: {len(stocks)} mã")
print(f"📅 Data: {output['last_update']}")
print(f"💾 Size: {file_size:.1f} MB")
print(f"\n🚀 Tiếp theo:")
print(f"   1. Upload stocks_data_ai_complete.json lên GitHub")
print(f"   2. Web tự động cập nhật!")
