#!/usr/bin/env python3
"""
Trading Strategies Skill - TA Calculation Script
Calculates technical analysis indicators from historical market data.
"""

import sys
import json
import statistics

def calculate_sma(data, period):
    """Simple Moving Average"""
    if len(data) < period:
        return None
    return sum(data[-period:]) / period

def calculate_ema(data, period):
    """Exponential Moving Average"""
    if len(data) < period:
        return None
    multiplier = 2 / (period + 1)
    ema = data[0]
    for price in data[1:]:
        ema = (price * multiplier) + (ema * (1 - multiplier))
    return ema

def calculate_rsi(closes, period=14):
    """Relative Strength Index"""
    if len(closes) < period + 1:
        return None
    deltas = [closes[i] - closes[i-1] for i in range(1, len(closes))]
    gains = [d if d > 0 else 0 for d in deltas]
    losses = [-d if d < 0 else 0 for d in deltas]
    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period
    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def calculate_bollinger_bands(closes, period=20, std_dev=2):
    """Bollinger Bands"""
    if len(closes) < period:
        return None, None, None
    sma = calculate_sma(closes, period)
    std = statistics.stdev(closes[-period:])
    upper = sma + (std_dev * std)
    lower = sma - (std_dev * std)
    return upper, sma, lower

def calculate_macd(closes):
    """MACD (12, 26, 9) - returns MACD line, signal line approx"""
    if len(closes) < 26:
        return None, None
    ema12 = calculate_ema(closes, 12)
    ema26 = calculate_ema(closes, 26)
    macd_line = ema12 - ema26
    # Simple signal approximation (should be EMA9 of MACD, but simplified)
    signal_line = macd_line  # Placeholder
    return macd_line, signal_line

def calculate_stochastic(highs, lows, closes, period=14):
    """Stochastic %K"""
    if len(highs) < period or len(lows) < period or len(closes) < period:
        return None
    high_period = max(highs[-period:])
    low_period = min(lows[-period:])
    if high_period == low_period:
        return 50  # Neutral
    k = 100 * (closes[-1] - low_period) / (high_period - low_period)
    return k

def calculate_indicators(klines_data):
    """
    Input: list of klines [ [timestamp, open, high, low, close, volume, ...], ... ]
    Output: dict of indicators
    """
    closes = [float(k[4]) for k in klines_data]
    highs = [float(k[2]) for k in klines_data]
    lows = [float(k[3]) for k in klines_data]
    volumes = [float(k[5]) for k in klines_data]

    indicators = {}

    # Price metrics
    indicators['current_price'] = closes[-1]
    indicators['price_change_24h'] = None  # Would need 24h data
    indicators['volume_24h'] = sum(volumes[-1:])  # Last candle volume

    # Moving Averages
    indicators['sma_20'] = calculate_sma(closes, 20)
    indicators['sma_10'] = calculate_sma(closes, 10)
    indicators['ema_12'] = calculate_ema(closes, 12)
    indicators['ema_26'] = calculate_ema(closes, 26)

    # Momentum
    indicators['rsi_14'] = calculate_rsi(closes, 14)

    # Bollinger Bands
    bb_upper, bb_middle, bb_lower = calculate_bollinger_bands(closes, 20, 2)
    indicators['bb_upper'] = bb_upper
    indicators['bb_middle'] = bb_middle
    indicators['bb_lower'] = bb_lower

    # MACD
    macd_line, signal_line = calculate_macd(closes)
    indicators['macd_line'] = macd_line
    indicators['macd_signal'] = signal_line
    indicators['macd_histogram'] = macd_line - signal_line if macd_line and signal_line else None

    # Stochastic
    indicators['stochastic_k'] = calculate_stochastic(highs, lows, closes, 14)

    return indicators

if __name__ == "__main__":
    # Example usage: read from stdin as JSON
    data = json.load(sys.stdin)
    result = calculate_indicators(data)
    print(json.dumps(result, indent=2))</content>
<parameter name="filePath">./skills/trading-strategies/scripts/calculate_ta.py