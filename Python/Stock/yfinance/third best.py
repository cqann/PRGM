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
cl = 573
for code in codes:
    if index > 100000: break
    code = code[:-1]
    current_stock = yf.Ticker(code)
    stock_history = current_stock.history("2y","1d")
    stock_names.append(code)
    stocks_history.append(stock_history)
    print(round(index/cl*100,2))
    index += 1

codes.close()
print("stocks loaded")

omx = yf.Ticker("^OMX")
omx_history = omx.history("2y","1d")
cash = 100
to_buy = ["","","","",""]
index = 0
days = list(omx_history.index.values)[:-1]
avg = []
for day in days: #days
    top_stocks = [(-100,""),(-100,""),(-100,""),(-100,""),(-100,"")]
    
    fifth_cash = cash / 5
    for i in range(len(stocks_history)):

        stock_history = stocks_history[i]
        try:
            str_day = str(day)
            current_day = stock_history.loc[[str_day]]
        except KeyError:
            continue
        stock_open = float(current_day["Open"])
        stock_close = float(current_day["Close"])
        stock_change = (stock_close) / stock_open

        if stock_names[i] == to_buy[2]:
            cash -= fifth_cash
            cash += fifth_cash * stock_change

        #creating todays winner list
        if top_stocks[0][0] >= stock_change: continue  
        index_in_list = bs.bisect_left(top_stocks, (stock_change, stock_names[i]))
        left_half = top_stocks[1:index_in_list]
        right_half = top_stocks[index_in_list:]
        top_stocks = left_half + [(stock_change, stock_names[i])] + right_half
        
    to_buy = [x[1] if x != (-100,"") else "" for x in top_stocks ]
    index += 1
    print(index//4.96, cash)
    if (index%(len(days)//20)) == 0:
        omx_open = float(omx_history.iloc[[index-len(days)//20]]["Open"])
        omx_close = float(omx_history.iloc[[index]]["Close"])
        print(round(cash/100,4), "OMX: ", omx_close/omx_open )
        avg.append((cash/100)/(omx_close/omx_open))
        cash = 100
    

print(avg)
print(sum(avg)/len(avg))