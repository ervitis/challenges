"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

O(n) & O(1) time complexity
"""
from typing import List


def max_profit(prices: List[int]) -> int:
    if len(prices) < 2:
        return 0

    buy = 0
    idx = 0
    for i in range(len(prices)-1):
        if prices[i+1] >= prices[i]:
            continue
        t = prices[i] - prices[buy]
        if t > idx:
            idx = t
        if prices[i+1] < prices[buy]:
            buy = i + 1
    t = prices[len(prices)-1] - prices[buy]
    if t > idx:
        idx = t
    return idx


if __name__ == '__main__':
    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max([7, 6, 4, 3, 1]))
