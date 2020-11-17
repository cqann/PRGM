from multiprocessing.pool import ThreadPool
import yfinance as yf
from tqdm import tqdm as progress_bar
import bisect as bs 

HISTORY = {}


def get_history(stock_code):
    current_stock = yf.Ticker(stock_code)
    HISTORY[stock_code] = current_stock.history("2y","1wk")
    # print(f"Getting data for {stock_code}...")

def main():
    stock_codes = []
    limit = 10000

    with open("codes.txt", "r") as codes_file:
        for code in codes_file:
            stock_codes.append(code[:-1])
            if len(stock_codes) >= limit: break

        with ThreadPool(120) as thread_pool:
            # Use a tqdm progress_bar
            for _ in progress_bar(thread_pool.imap_unordered(get_history, stock_codes), total=len(stock_codes), desc="Gathering Stock History"):
                pass

    omx = yf.Ticker("^OMX")
    omx_history = omx.history("2y","1wk")[:-1]

    cash = 1
    to_buy = set()
    index = 0
    days = list(omx_history.index.values)[:-1]
    avg = []
    for day in days: #days
        top_stocks = [(-100,""),(-100,""),(-100,""),(-100,""),(-100,"")]

        fifth_cash = cash / 5
        i = 0
        for stock_code in HISTORY:

            stock_history = HISTORY[stock_code]
            try:
                str_day = str(day)
                current_day = stock_history.loc[[str_day]]
                if len(current_day["Open"]) != 1:
                    current_day = current_day[0]
            except KeyError:
                i += 1
                continue
            
            stock_open = float(current_day["Open"])
            stock_close = float(current_day["Close"])
            stock_change = (stock_close) / stock_open

            if stock_code in to_buy:
                cash -= fifth_cash
                cash += fifth_cash * stock_change

            #creating todays winner list
            if top_stocks[0][0] >= stock_change: i+=1; continue  
            index_in_list = bs.bisect_left(top_stocks, (stock_change, stock_code))
            left_half = top_stocks[1:index_in_list]
            right_half = top_stocks[index_in_list:]
            top_stocks = left_half + [(stock_change, stock_code)] + right_half
            
        to_buy = set([x[1]  for x in top_stocks if x != (-100,"")])
        index += 1
        omx_open = float(omx_history.iloc[[index]]["Open"])
        omx_close = float(omx_history.iloc[[index]]["Close"])
        omx_change = omx_open/omx_close
        if omx_change == 0:
            print(omx_open, omx_open, omx_change)
        avg.append((cash)/(1))
        cash = 1
        

    print(avg)
    print(sum(avg)/len(avg))


if __name__ == "__main__":
    main()
