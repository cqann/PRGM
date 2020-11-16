import yfinance as yf

loomis = yf.Ticker("^OMX")
h = loomis.history("1mo","1d")
volvo = yf.Ticker("DUNi.ST")
volv_his = volvo.history("1mo", "1d")


for i in list(h.index.values):
    i = str(i)
    a = volv_his.loc[[i]]
    stock_open = float(a["Open"])
    print(stock_open)

