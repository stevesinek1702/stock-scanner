#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stock Scanner - Tìm cổ phiếu gần hoặc cắt MA100/MA200
"""

import requests
import pandas as pd
from datetime import datetime, timedelta
import time
import os
import json

# Headers chuẩn cho FireAnt API
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://fireant.vn/",
}

def fetch_historical_data(symbol, days=250):
    """Lấy dữ liệu lịch sử từ FireAnt API"""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    url = f"https://www.fireant.vn/api/Data/Companies/HistoricalQuotes"
    params = {
        "symbol": symbol,
        "startDate": start_date.strftime("%Y-%m-%d"),
        "endDate": end_date.strftime("%Y-%m-%d")
    }
    
    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data and len(data) > 0:
                df = pd.DataFrame(data)
                # Sắp xếp theo ngày tăng dần
                df = df.sort_values('date')
                return df
    except Exception as e:
        print(f"❌ Lỗi {symbol}: {e}")
    
    return None

def calculate_ma(df, period):
    """Tính Moving Average"""
    if len(df) < period:
        return None
    return df['close'].rolling(window=period).mean()

def check_near_ma(close, ma, threshold=0.01):
    """Kiểm tra giá có gần MA không (±1%)"""
    if pd.isna(ma):
        return False
    diff_percent = abs(close - ma) / ma
    return diff_percent <= threshold

def check_golden_cross(df, ma_period):
    """Kiểm tra cắt lên MA (golden cross)
    
    Điều kiện:
    - Phiên trước: close < MA
    - Phiên hiện tại: close > MA
    """
    if len(df) < ma_period + 1:
        return False
    
    ma = calculate_ma(df, ma_period)
    if ma is None or len(ma) < 2:
        return False
    
    # Lấy 2 phiên gần nhất
    prev_close = df['close'].iloc[-2]
    curr_close = df['close'].iloc[-1]
    prev_ma = ma.iloc[-2]
    curr_ma = ma.iloc[-1]
    
    if pd.isna(prev_ma) or pd.isna(curr_ma):
        return False
    
    # Cắt lên: trước đó dưới MA, hiện tại trên MA
    return prev_close < prev_ma and curr_close > curr_ma

def scan_symbol(symbol):
    """Quét 1 mã cổ phiếu"""
    print(f"🔍 Đang quét {symbol}...", end=" ")
    
    df = fetch_historical_data(symbol, days=250)
    if df is None or len(df) < 200:
        print("❌ Không đủ dữ liệu")
        return None
    
    # Lấy giá đóng cửa mới nhất
    latest_close = df['close'].iloc[-1]
    latest_date = df['date'].iloc[-1]
    
    # Tính MA100 và MA200
    ma100 = calculate_ma(df, 100)
    ma200 = calculate_ma(df, 200)
    
    if ma100 is None or ma200 is None:
        print("❌ Không tính được MA")
        return None
    
    latest_ma100 = ma100.iloc[-1]
    latest_ma200 = ma200.iloc[-1]
    
    # Kiểm tra các điều kiện
    near_ma100 = check_near_ma(latest_close, latest_ma100, 0.01)
    near_ma200 = check_near_ma(latest_close, latest_ma200, 0.01)
    cross_ma100 = check_golden_cross(df, 100)
    cross_ma200 = check_golden_cross(df, 200)
    
    # Tính % chênh lệch
    diff_ma100_pct = ((latest_close - latest_ma100) / latest_ma100 * 100) if not pd.isna(latest_ma100) else 0
    diff_ma200_pct = ((latest_close - latest_ma200) / latest_ma200 * 100) if not pd.isna(latest_ma200) else 0
    
    signals = []
    if near_ma100:
        signals.append("Gần MA100")
    if near_ma200:
        signals.append("Gần MA200")
    if cross_ma100:
        signals.append("Cắt lên MA100")
    if cross_ma200:
        signals.append("Cắt lên MA200")
    
    if signals:
        print(f"✅ {', '.join(signals)}")
        return {
            "Symbol": symbol,
            "Date": latest_date,
            "Close": round(latest_close, 2),
            "MA100": round(latest_ma100, 2),
            "MA200": round(latest_ma200, 2),
            "Diff_MA100_%": round(diff_ma100_pct, 2),
            "Diff_MA200_%": round(diff_ma200_pct, 2),
            "Near_MA100": "✓" if near_ma100 else "",
            "Near_MA200": "✓" if near_ma200 else "",
            "Cross_MA100": "✓" if cross_ma100 else "",
            "Cross_MA200": "✓" if cross_ma200 else "",
            "Signals": " | ".join(signals)
        }
    else:
        print("⚪ Không có tín hiệu")
        return None

def main():
    print("=" * 60)
    print("📊 STOCK SCANNER - MA100/MA200")
    print("=" * 60)
    print(f"⏰ Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Đọc danh sách mã
    if os.path.exists("symbols.txt"):
        with open("symbols.txt", "r") as f:
            symbols = [line.strip() for line in f if line.strip()]
    else:
        print("❌ Không tìm thấy file symbols.txt")
        return
    
    print(f"📋 Tổng số mã: {len(symbols)}")
    print()
    
    results = []
    for i, symbol in enumerate(symbols, 1):
        print(f"[{i}/{len(symbols)}] ", end="")
        result = scan_symbol(symbol)
        if result:
            results.append(result)
        
        # Nghỉ 0.5s giữa các request để tránh rate limit
        if i < len(symbols):
            time.sleep(0.5)
    
    print()
    print("=" * 60)
    print(f"✅ Hoàn tất! Tìm thấy {len(results)} tín hiệu")
    print("=" * 60)
    
    # Lưu kết quả
    if results:
        df_results = pd.DataFrame(results)
        
        # Tạo thư mục results nếu chưa có
        os.makedirs("results", exist_ok=True)
        
        # Lưu CSV
        csv_path = "results/latest.csv"
        df_results.to_csv(csv_path, index=False, encoding="utf-8-sig")
        print(f"💾 Đã lưu: {csv_path}")
        
        # Lưu JSON
        json_path = "results/latest.json"
        df_results.to_json(json_path, orient="records", force_ascii=False, indent=2)
        print(f"💾 Đã lưu: {json_path}")
        
        # In bảng kết quả
        print()
        print("📊 KẾT QUẢ:")
        print(df_results.to_string(index=False))
    else:
        print("⚠️ Không tìm thấy tín hiệu nào")

if __name__ == "__main__":
    main()
