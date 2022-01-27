import yfinance as yf

loomis = yf.Ticker("^OMX")
h = loomis.history("1mo","1d")
volvo = yf.Ticker("VOLV-A.ST")
volv_his = volvo.history("1y", "60m")
print(volv_his)