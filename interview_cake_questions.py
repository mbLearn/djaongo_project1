import itertools

# Interview Cake Questions

# 1. Suppose we could access yesterday's stock prices as a list, where:

# The indices are the time in minutes past trade opening time, which was 9:30am local time.
# The values are the price in dollars of Apple stock at that time.
# So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

# Write an efficient function that takes stock_prices_yesterday and returns the best profit
# I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

# stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
# stock_prices_yesterday2 = [13, 10, 7, 5, 8, 19, 9]
# stock_prices_yesterday3 = [13, 10]
#
# # def get_max_profit(stock_prices_yesterday):
# #     min_index = stock_prices_yesterday.index(min(stock_prices_yesterday))
# #     max_index = stock_prices_yesterday.index(max(stock_prices_yesterday))
# #
# #     best_price = stock_prices_yesterday[max_index]- stock_prices_yesterday[min_index]
# #     return best_price
# #
# # print get_max_profit(stock_prices_yesterday)
#
#
# def smallest_num_in_list( list ):
#     min = list[ 0 ]
#     for a in list:
#         if a < min:
#             min = a
#     return min
# #print(smallest_num_in_list([1, 2, -8, 0, 11, 0, -9, 9, -7]))
#
# def biggest_num_in_list( list ):
#     max = list[ 0 ]
#     for a in list:
#         if a > max:
#             max = a
#     return max
# #print(smallest_num_in_list([1, 2, -8, 0, 11, 0, -9, 9, -7]))
#
#
#
# def get_max_profit(stock_prices):
#     min_index = stock_prices.index(min(stock_prices))
#     max_index = stock_prices.index(max(stock_prices[min_index:]))
#
#     best_price = stock_prices[max_index] - stock_prices[min_index]
#     return best_price
#
# print get_max_profit(stock_prices_yesterday)
# print get_max_profit(stock_prices_yesterday2)
# print get_max_profit(stock_prices_yesterday3)
#
#
# def get_maximum_profit(stock_prices_list):
#     min_index_1 = stock_prices_list.index(smallest_num_in_list(stock_prices_list))
#     max_index_1 = stock_prices_list.index(biggest_num_in_list(stock_prices_list[min_index_1:]))
#     potential_best = stock_prices_list[max_index_1] - stock_prices_list[min_index_1]
#
#     best_profit = max(0,potential_best)
#     return best_profit
#
#
# print get_maximum_profit(stock_prices_yesterday)
# print get_maximum_profit(stock_prices_yesterday2)
# print get_maximum_profit(stock_prices_yesterday3)



## Write a function get_products_of_all_ints_except_at_index()
# that takes a list of integers and returns a list of the products.


#prices = [0,1,23,4,5,6,90,0,1,2,-1]


#def get_max_profit3(st_prices):
    # find the maximum from the list
    #max_price = st_prices[0]
    #max_index = 0
    #for i,val in enumerate(st_prices):
    #    if val > max_price:
    #        max_price = val
    #        max_index = i


    #my_current_index_at_max = max_index

    #min_price = st_prices[0]
    #min_index = 0
    #for i, min_val in enumerate(st_prices[0:max_index]):
    #    if min_val < min_price:
    #        min_val = min_price
    #        min_index = i
    #print min_price

    #optimal_gain = max_price - min_price
    #print optimal_gain
    #best_gain = max(0,optimal_gain)

#    return best_gain


#print get_max_profit3(prices)
# 90

#print get_max_profit3([10,4])
# 0

#print get_max_profit3([-9,-10,-11,-1,-2])
# 8

#print get_max_profit3([0,12,3,4,5,6,10,12])
# 12

#print get_max_profit3([0,1,0,-10,0])
# 1

#print get_max_profit3([100000,-10,10])
# 0

#print get_max_profit3([10,9,5,2,6,0])
#0

import doctest

# def find_profit(stock_price):
#     """
#
#     :param lst: list of stock price
#     :return: maximum profit
#
#     >>> find_profit([100000,-10,10])
#     20
#     >>> find_profit([0,1,0,-10,0])
#     10
#     >>> find_profit([-9,-10,-11,-1,-2])
#     10
#     >>> find_profit([10,4])
#     -6
#     >>> find_profit([0,1,23,4,5,6,90,0,1,2,-1])
#     90
#     >>> find_profit([10,8,6,4,3])
#     -1
#     >>> find_profit([10,8,-2])
#     -2
#
#     """
#     max_profit = 0
#
#     # go through every price (with its index as the time)
#     for earlier_time, earlier_price in enumerate(stock_price):
#
#
#         # and go through all the LATER prices
#         for later_time in xrange(earlier_time + 1, len(stock_price)):
#             later_price = stock_price[later_time]
#
#             # see what our profit would be if we bought at the
#             # earlier price and sold at the later price
#             potential_profit = later_price - earlier_price
#
#             # update max_profit if we can do better
#             max_profit = max(max_profit, potential_profit)
#
#     return max_profit
#
#
def find_profit1(stock_price):
    """

    :param lst: list of stock price
    :return: maximum profit

   >>> find_profit1([100000,-10,10])
   20
   >>> find_profit1([0,1,0,-10,0])
   10
   >>> find_profit1([-9,-10,-11,-1,-2])
   10
   >>> find_profit1([10,4])
   -6
   >>> find_profit1([0,1,23,4,5,6,90,0,1,2,-1])
   90
   >>> find_profit1([10,4,2,4,0])
   2
   >>> find_profit1([10,-4,-12])
   -8
   >>> find_profit1([10,8,6,4,3])
   -1

    """
    buy_price = stock_price[0]
    max_profit = stock_price[1]-stock_price[0]



    for i, current_price in enumerate(stock_price[:-1]):
        buy_price = min(buy_price, current_price)

        potential_profit = stock_price[i+1] - buy_price
        max_profit = max(max_profit, potential_profit)

    return max_profit



def find_profit4(stock_prices):
   """
   >>> find_profit4([100000,-10,10])
   20
   >>> find_profit4([0,1,0,-10,0])
   10
   >>> find_profit4([-9,-10,-11,-1,-2])
   10
   >>> find_profit4([10,4])
   -6
   >>> find_profit4([0,1,23,4,5,6,90,0,1,2,-1])
   90
   >>> find_profit4([10,4,2,4,0])
   2
   >>> find_profit4([10,-4,-12])
   -8
   >>> find_profit4([10,8,6,4,3])
   -1
   """
   new_list = []
   if len(stock_prices) > 2:
       for a,b in itertools.combinations(stock_prices,2):
           new_list.append(b-a)
       #print new_list
       return max(new_list)
   else:
       return stock_prices[1]-stock_prices[0]





# def move_0_at_the_end(lst):
#     """
#     >>> move_0_at_the_end([1,0,2,3,0,4,5,0])
#     # [1, 2, 3, 4, 5, 0, 0, 0]
#     """
#
#     number_of_occurance = lst.count(0)
#
#     for i, y in enumerate(lst):
#         if y == 0:
#             del lst[i]
#
#     for x in range(number_of_occurance):
#             lst.append(0)
#
#     return lst



if __name__ == "__main__":
    import doctest
    doctest.testmod()
