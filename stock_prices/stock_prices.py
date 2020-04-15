#!/usr/bin/python

import argparse

prices = [2, 8, 3, 5, 10]


def find_max_profit(prices):

    # input = list of stock prices

    # keep track of the current min price so far as we loop through

    current_min_price = prices[0]
    current_max_profit = prices[1] - prices[0]
    for i in range(0, len(prices)):
        if prices[i] < current_min_price:
            current_min_price = prices[i]
        if prices[i] - current_min_price > current_max_profit and prices[i] != current_min_price:
            current_max_profit = prices[i] - current_min_price

    return current_max_profit


print(find_max_profit([1050, 270, 1540, 3800, 2]))


# output = find max profit

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
