from itertools import * 
# You have an endless supply of dimes and pennies. How many different amounts of total change can you make using exactly num_coins number coins?
# For example, when num_coins = 3, you can create 4 different kinds of change:
# 3 cents from penny + penny + penny
# 12 cents dime + penny + penny
# 21 cents from dime + dime + penny
# 30 cents from dime + dime + dime
# So, you should have a function that returns the set {3, 12, 21, 30} when num_coins is 3

def change_quant(num_coins):
    change_val = {'penny': 1, 'dime':10
    }
    values = list(change_val.values())
    perm = combinations_with_replacement(values,num_coins) 
    output = set()
    for i in list(perm):
        output.add(sum(i))
    print(output)
change_quant(3)

        
        
        
        
        
  

                    


