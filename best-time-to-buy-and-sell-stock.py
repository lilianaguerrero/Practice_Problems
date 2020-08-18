# -input of stock prices
#         -output of max profit
        
#         -conditionas are that must buy before you sell
#         -just buy once sell once
#         -positive integers
#         -assume there is profit to be made
#         -[5,4,3,2,1] yes
        
#         -approach
#         -keep track of the lowest price, start by iterating at index 0
#         -current profit = starting price at index 1 - lowest price
#         -max profit by comparing it to the current profit
#         -returning htee max profit
        
        if len(prices) < 2:
            return 0
        
        lowest_price = prices[0]
        max_profit = prices[1] - prices[0]
        
        for current_price in prices:
            if current_price < lowest_price:
                lowest_price = current_price
            current_profit = current_price - lowest_price
            max_profit = max(max_profit, current_profit)
            
        return max_profit
                