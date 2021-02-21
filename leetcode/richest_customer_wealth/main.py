"""

"""
from typing import List


def maximum_wealth(accounts: List[List[int]]) -> int:
    m = 0
    for account in accounts:
        curr = 0
        for e in account:
            curr += e
        m = max(m, curr)
    return m


if __name__ == '__main__':
    print(maximum_wealth([[1, 2, 3], [3, 2, 1]]))
    print(maximum_wealth([[1, 5], [7, 3], [3, 5]]))
    print(maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
