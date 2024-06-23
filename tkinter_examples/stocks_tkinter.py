import tkinter as tk
from tkinter import ttk
import urllib.request
import json

# alphavantage
API_KEY = ""  # Get your free API key from Alpha Vantage
FUNCTION = "TIME_SERIES_INTRADAY"
INTERVAL = "1min"

def fetch_and_display_stock_data():  # Triggered by combobox selection
    print('callback')
    symbol = ticker_combobox.get()
    print('symbol:', symbol)
    url = f"https://www.alphavantage.co/query?function={FUNCTION}&symbol={symbol}&interval={INTERVAL}&apikey={API_KEY}"
    response = urllib.request.urlopen(url)

    if response.getcode() == 200:
        data = json.loads(response.read())
        print(data)
        time_series = data["Time Series (1min)"]
        latest_time, latest_data = next(iter(time_series.items()))
        price = latest_data["4. close"]
        result_label.config(text=f"Latest Price for {symbol}: {price}")
    else:
        result_label.config(text="Error fetching data")

def item_selected(event=None):
    print('value selected')

# Create main window
window = tk.Tk()
window.title("Stock Ticker App")

# Stock Ticker Selection
tk.Label(window, text="Select Stock Ticker:").pack(pady=10)
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]  # Add more as needed
ticker_combobox = ttk.Combobox(window, values=tickers)
ticker_combobox.pack()
# ticker_combobox.bind("<<ComboboxSelected>>", item_selected)
ticker_combobox.bind("<ButtonRelease-1>", item_selected)



button = tk.Button(window, text="GET DATA", command=fetch_and_display_stock_data)
button.pack()

# Result Label
result_label = tk.Label(window, text="RESULT will be displayed here")
result_label.pack(pady=20)

window.mainloop()
