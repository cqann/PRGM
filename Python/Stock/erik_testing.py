from multiprocessing.pool import ThreadPool
import yfinance as yf
from tqdm import tqdm as progress_bar

HISTORY = {}


def get_history(stock_code):
    current_stock = yf.Ticker(stock_code)
    HISTORY[stock_code] = current_stock.history("2y","1d")
    # print(f"Getting data for {stock_code}...")

def main():
    stock_codes = []
    limit = 40

    with open("codes.txt", "r") as codes_file:
        for code in codes_file:
            stock_codes.append(code[:-1])
            if len(stock_codes) >= limit: break

        with ThreadPool(120) as thread_pool:
            # Use a tqdm progress_bar
            for _ in progress_bar(thread_pool.imap_unordered(get_history, stock_codes), total=len(stock_codes), desc="Gathering Stock History"):
                pass

    omx = yf.Ticker("^OMX")
    omx_history = omx.history("2y","1d")


if __name__ == "__main__":
    main()
