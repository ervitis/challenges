"""
Given an integer n, return the number of trailing zeroes in n!.
"""


def trailing_zeroes(n: int) -> int:
    c = 0

    while n > 0:
        n //= 5
        c += n
    return c


if __name__ == '__main__':
    print(trailing_zeroes(3))
    print(trailing_zeroes(5))
    print(trailing_zeroes(0))
    print(trailing_zeroes(120))
