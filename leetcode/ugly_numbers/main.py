"""
Given an integer n, return true if n is an ugly number.

Ugly number is a positive number whose prime factors only include 2, 3, and/or 5.
"""


def is_ugly(n: int) -> bool:
    if n <= 0:
        return False
    if n == 1:
        return True

    while n > 1:
        if n % 2 == 0:
            n //= 2
        elif n % 3 == 0:
            n //= 3
        elif n % 5 == 0:
            n //= 5
        else:
            return False
    return True


if __name__ == '__main__':
    print(is_ugly(6))
    print(is_ugly(8))
    print(is_ugly(14))
