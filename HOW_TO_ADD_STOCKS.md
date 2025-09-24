# 📈 How to Add or Change Stocks in Your Tracker

## 🎯 **Quick Summary - You Have 4 Ways:**

### 1. 🚀 **Quick Add (Easiest) - Preserves All Existing Stocks**
```bash
py add_stocks.py AAPL GOOGL MSFT TSLA NVDA
```
✅ **Fixed!** Now adds to existing stocks instead of replacing them.

### 2. ⚙️ **Edit Configuration File**
Open `config.py` and modify the `DEFAULT_SYMBOLS` list:
```python
DEFAULT_SYMBOLS = [
    'SPY', 'QQQ', 'GLD', 'ARKK', 'TLT',  # ETFs
    'AAPL', 'GOOGL', 'MSFT', 'TSLA', 'NVDA'  # Individual stocks
]
```

### 3. 💻 **Interactive Mode**
```bash
py add_stocks.py
# Then enter symbols when prompted: AAPL,GOOGL,MSFT
```

### 4. 📊 **Custom Python Script**
```python
from stock_tracker import StockTracker
tracker = StockTracker(['YOUR', 'CUSTOM', 'SYMBOLS'])
tracker.run_update()
```

---

## 📊 **Your Current Portfolio:**

### ETFs (Exchange Traded Funds):
- **SPY** - S&P 500 Index ($663.21, -0.54%)
- **QQQ** - NASDAQ 100 Index ($598.20, -0.66%)
- **GLD** - Gold ETF ($346.46, +0.41%)
- **ARKK** - Innovation ETF ($83.58, -1.31%)
- **TLT** - Long-term Treasury ($89.32, +0.70%)

### Individual Stocks:
- **AAPL** - Apple Inc. ($254.43, -0.64%)
- **GOOGL** - Alphabet/Google ($251.66, -0.34%)
- **MSFT** - Microsoft ($509.23, -1.01%)
- **TSLA** - Tesla ($425.85, -1.93%)
- **NVDA** - NVIDIA ($178.43, -2.82%)

---

## 🔧 **How to Add More Stocks:**

### Popular Stock Categories:

#### Tech Giants:
```bash
python add_stocks.py AMZN META NFLX
```

#### Banking & Finance:
```bash
python add_stocks.py JPM BAC WFC GS
```

#### Healthcare:
```bash
python add_stocks.py JNJ PFE UNH ABBV
```

#### Crypto-Related:
```bash
python add_stocks.py COIN MSTR RIOT MARA
```

#### International:
```bash
python add_stocks.py BABA TSM ASML NVO
```

#### Dividend Stocks:
```bash
python add_stocks.py KO PEP JNJ PG
```

---

## 📁 **What Happens When You Add Stocks:**

1. **New Excel Files Created**: Each stock gets its own `.xlsx` file
2. **Dashboard Updated**: Web dashboard shows new stocks automatically
3. **Power BI Ready**: Consolidated data files include new stocks
4. **Historical Data**: 1 year of price/volume data fetched

---

## 🎨 **Customize Portfolio Weights:**

Edit `config.py` to set custom allocation percentages:

```python
PORTFOLIO_WEIGHTS = {
    'AAPL': 0.20,   # 20% allocation
    'GOOGL': 0.15,  # 15% allocation
    'MSFT': 0.15,   # 15% allocation
    # ... add your desired weights
}
```

---

## 🔄 **Remove Stocks:**

To stop tracking certain stocks, edit `config.py` and remove them from `DEFAULT_SYMBOLS`, then run:
```bash
python stock_tracker.py
```

---

## ⚡ **Quick Commands:**

```bash
# Add single stock
python add_stocks.py TSLA

# Add multiple stocks
python add_stocks.py AAPL GOOGL MSFT TSLA NVDA

# Update all tracked stocks
python stock_tracker.py

# Start web dashboard
python -m streamlit run dashboard.py

# Start automated updates
python scheduler.py
```

---

## 🎯 **Pro Tips:**

1. **Start Small**: Add 5-10 stocks initially
2. **Mix Categories**: Combine ETFs with individual stocks
3. **Regular Updates**: Use scheduler for automatic data refresh
4. **Check Symbols**: Verify ticker symbols on Yahoo Finance first
5. **Backup Data**: Your Excel files contain all historical data

---

## 🚨 **Valid Stock Symbols:**

- Use official ticker symbols (e.g., AAPL not Apple)
- Check Yahoo Finance for correct symbols
- Most US stocks work (NYSE, NASDAQ)
- International stocks: add exchange suffix (e.g., ASML.AS)

Your stock tracker is now fully customizable! 🚀📈