"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""


def is_power_of_four(n: int) -> bool:
    if n == 0:
        return False

    while n != 1:
        if n % 4 != 0:
            return False
        n //= 4
    return True


if __name__ == '__main__':
    print(is_power_of_four(16))
    print(is_power_of_four(8))
    print(is_power_of_four(5))
    print(is_power_of_four(4096))
