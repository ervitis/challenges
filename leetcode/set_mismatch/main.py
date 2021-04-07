"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""
from collections import Counter
from typing import List


def find_error_nums(nums: List[int]) -> List[int]:
    d = {}
    r = []
    for num in nums:
        if d.get(num):
            r.append(num)
            break
        else:
            d[num] = 1
    r.append(sum(range(1, len(nums) + 1)) - (sum(nums) - r[0]))
    return r


if __name__ == '__main__':
    print(find_error_nums([1, 2, 2, 4]))
    print(find_error_nums([1, 1]))
    print(find_error_nums([2, 2]))
    print(find_error_nums([3, 2, 3, 4, 6, 5]))
