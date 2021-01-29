"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only
the integer part of the result is returned.
"""


def my_sqrt(x: int) -> int:
    if x < 2:
        return x
    i = 1

    while i * i <= x:
        i += 1
    i -= 1

    return int(i)


if __name__ == '__main__':
    print(my_sqrt(4))
    print(my_sqrt(8))
    print(my_sqrt(9))
    print(my_sqrt(81))
    print(my_sqrt(1))
