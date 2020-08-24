# Stock Prices

# You want to write a bot that will automate the task of day-trading for you while you're going through Lambda. You decide to have your bot just # focus on buying and selling Amazon stock. 

# Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

# For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices.

# For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes before it; it can't come after it in the list of prices.

# def find_max_profit(prices):
#     # first, find the greatest value in the array
#     max_stock_price = max(prices)
#     # since max profit is computed by taking max_stock_price
#     # and subtracting from it the smallest value that comes
#     # before it in the array (cannot come after it),
#     # grab array slice that ends at max_stock_price and find 
#     # min value of that slice
#     previous_prices = prices[ : prices.index(max_stock_price)]

#     copy_of_prices = [i for i in prices] 

#     if len(previous_prices) > 0:
#         min_stock_price = min(previous_prices)
#         return max_stock_price - min_stock_price
#     elif len(previous_prices) == 0 and len(prices) > 1:
#         # if the greatest value came first,
#         # search again but use the array without max_stock_price
#         prices_minus_max = [i for i in prices if i != max_stock_price]
#         return find_max_profit(prices_minus_max)
#     elif len(previous_prices) == 0 and len(prices) == 1:
#         # stock prices are going down and there will be no profit,
#         # find the smallest loss
#         smallest_loss = 0
#         for price, i in copy_of_prices[1:]:
#             this_slice = [each for each in copy_of_prices[:i]]
#             this_min = min(this_slice)
#             this_difference = price - this_min
#             if smallest_loss == 0:
#                 smallest_loss = this_difference
#             else:
#                 if smallest_loss < this_difference:
#                     smallest_loss = this.difference
#         print(smallest_loss)            
#         return smallest_loss        
# 
# another attempt

def find_max_profit(prices):
    max_profit_val, current_max_val = 0, 0 
    for price in reversed(prices):                       
        current_max_val = max(current_max_val, price)          
        potential_profit = current_max_val - price          
        max_profit_val = max(potential_profit, max_profit_val)

    if max_profit_val > 0:
        return max_profit_val
    else:    
        biggest_loss = 0 - current_max_val
        for price in reversed(prices):
            current_max_val = max(current_max_val, price)          
            potential_profit = current_max_val - price         
            max_profit_val = max(potential_profit, max_profit_val)

        return biggest_loss + max_profit_val


# third attempt

# def find_max_profit(prices):
#     # Store the best possible profit we can make; initially this is 0.
#     bestProfit = 0;

#     # Iterate across all pairs and find the best out of all of them.  As a
#     # minor optimization, we don't consider any pair consisting of a single
#     # element twice, since we already know that we get profit 0 from this.
#     for i in range(0, len(prices)):
#         for j in range (i + 1, len(prices)):
#             bestProfit = max(bestProfit, prices[j] - prices[i])

#     return bestProfit


print(find_max_profit([10, 7, 5, 8, 11, 9])) # ---> 6
print(find_max_profit([100, 90, 80, 50, 20, 10])) # ---> -10
print(find_max_profit([1050, 270, 1540, 3800, 2])) # ---> 3530
print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79])) # ---> 94