"""
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
O(n) & O(1) time complexity
"""
from typing import List


def max_profit(prices: List[int]) -> int:
    idx = 0
    for i in range(1, len(prices)):
        if prices[i] - prices[i - 1] > 0:
            idx += prices[i] - prices[i - 1]
    return idx


if __name__ == '__main__':
    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([1, 2, 3, 4, 5]))
    print(max_profit([7, 6, 4, 3, 1]))
