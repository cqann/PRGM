import yfinance as yf
import bisect as bs
def check_if_valid(code):
    try:
        test = yf.Ticker(code)
        var = test.info
        return True
    except:
        return False

stock_names = []
stocks_history = []
codes = open("codes.txt","r")
index = 0
days = 0
cl = 573
for code in codes:
    code = code[:-1]
    print(code)
    current_stock = yf.Ticker(code)
    stock_history = current_stock.history("1mo","1d")
    stock_names.append(code)
    stocks_history.append(stock_history)
    days = len(stock_history)-1
    print(round(index/cl*100,2))
    index += 1

codes.close()
print("stocks loaded")

for day in range(days,0,-1):
    top_stocks = [(-100,""),(-100,""),(-100,""),(-100,""),(-100,"")]
    for i in range(len(stocks_history)):
        stock_history = stocks_history[i]
        current_day = stock_history.iloc[[day]]
        stock_open = float(current_day["Open"])
        stock_close = float(current_day["Close"])
        stock_change = (stock_close - stock_open) / stock_open
        if top_stocks[0][0] > stock_change: continue
        
        #creating todays winner list
        index_in_list = bs.bisect_left(top_stocks, (stock_change, stock_names[i]))
        left_half = top_stocks[1:index_in_list]
        right_half = top_stocks[index_in_list:]
        top_stocks = left_half + [(stock_change, stock_names[i])] + right_half
    print(top_stocks)
    break
