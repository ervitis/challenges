"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
"""
from typing import List


def check_if_exists(arr: List[int]) -> bool:
    mult = set()
    for e in arr:
        if 2 * e in mult:
            return True
        elif e % 2 == 0 and e // 2 in mult:
            return True
        elif e == 0 and 0 in mult:
            return True
        else:
            mult.add(e)
    return False


if __name__ == '__main__':
    print(check_if_exists([10, 2, 5, 3]))
    print(check_if_exists([7, 1, 14, 11]))
