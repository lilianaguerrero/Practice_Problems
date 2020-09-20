stock_prices = [10, 7, 5, 2, 1, 1]
stock_prices1 = [1, 7, 5, 8, 1, 1]
stock_prices2 = [2, 7, 1, 8, 0, 1]

def get_max_profit(stock_prices):
    buy_times = []
    buy_time = 0
    sell_time = 0
    length = len(stock_prices)
    if length < 2:
        return 0
    low_price = stock_prices[0]
    max_profit = 0
    for i in range(1,length):
        curr_price = stock_prices[i]
        if curr_price < low_price:
            low_price = curr_price
            buy_times.append(i)
        current_prof = curr_price - low_price
        if current_prof > max_profit:
            max_profit = curr_price - low_price
            sell_time = i
        for n in buy_times:
            if stock_prices[sell_time] - max_profit == stock_prices[n]:
                buy_time = n
    return max_profit, sell_time, buy_time
print(get_max_profit(stock_prices2))

        
    














































    # for val in stock_prices:
    #     buy = min(stock_prices[:-1])
    #     buy_time = stock_prices.index(buy)
    #     sell = max(stock_prices[buy_time:])
    #     print(buy_time)
    # print(sell - buy)

