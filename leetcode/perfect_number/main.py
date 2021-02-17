"""
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.
"""
from math import sqrt


def check_perfect_number(num: int) -> bool:
    if num <= 1:
        return False

    c = int(sqrt(num))
    s = 1

    for i in range(2, c + 1):
        if num % i == 0:
            s += i + num / i

    return num == s


if __name__ == '__main__':
    print(check_perfect_number(28))
    print(check_perfect_number(496))
    print(check_perfect_number(8128))
