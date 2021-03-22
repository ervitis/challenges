"""
Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.
"""
from typing import List


def final_prices(prices: List[int]) -> List[int]:
    n = len(prices)
    res = []
    for i in range(n - 1):
        j = i + 1
        while j < n - 1 and prices[j] > prices[i]:
            j += 1
        if j == n - 1 and prices[j] > prices[i]:
            res.append(prices[i])
        else:
            res.append(prices[i] - prices[j])
    return res + [prices[n - 1]]


if __name__ == '__main__':
    print(final_prices([8, 4, 6, 2, 3]))
    print(final_prices([1, 2, 3, 4, 5]))
