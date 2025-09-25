import yfinance as yf

ticker = yf.Ticker("URA")
hist = ticker.history(period="1d", interval="1m")
print(hist)