stock_prices = [10, 7, 5, 2, 1, 1]

def get_max_profit(stock_prices):
    for val in stock_prices:
        buy = min(stock_prices[:-1])
        buy_time = stock_prices.index(buy)
        sell = max(stock_prices[buy_time:])
        print(buy_time)
    print(sell - buy)

