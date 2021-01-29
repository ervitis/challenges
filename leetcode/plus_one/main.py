"""
Given a non-empty array of decimal digits representing a non-negative integer,
increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""
from typing import List


def plus_one(digits: List[int]) -> List[int]:
    s = 1
    for i in range(len(digits)-1, -1, -1):
        digits[i] += s
        s = digits[i] // 10
        digits[i] %= 10

    if s == 1:
        digits.insert(0, s)
    return digits


if __name__ == '__main__':
    # plus_one([1, 2, 3])
    # plus_one([4, 3, 2, 1])
    # print(plus_one([4, 3, 2, 9]))
    print(plus_one([9, 9, 9, 9]))
    print(plus_one([0]))
