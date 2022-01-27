import yfinance as yf
import bisect as bs
import pandas as pd
import random

def check_if_valid(code):
    try:
        test = yf.Ticker(code)
        var = test.info
        return True
    except:
        return False

code = "VOLV-A.ST"
print(code)
current_stock = yf.Ticker(code)
history = current_stock.history(period = "max")
history = history.drop(columns = ["Dividends", "Stock Splits"])
for i, day in history.iterrows():
    if day["Volume"] == 0 : 
        history = history.drop([i])

chunks = []
chunk_size = 5
for i in range(0, len(history), chunk_size):
    if i + chunk_size >= len(history): break
    chunks.append(history[i:i+chunk_size])

scrambled_chunks = chunks[:]
random.shuffle(scrambled_chunks)
print(scrambled_chunks)