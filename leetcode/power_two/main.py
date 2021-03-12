"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""


def is_power_of_two(n: int) -> bool:
    if n <= 0:
        return False

    for i in range(n+1):
        d = i // 1 << (n.bit_length()-1)
        if d == n:
            return True
        if d > n:
            return False
    return False


if __name__ == '__main__':
    print(is_power_of_two(1))
    print(is_power_of_two(16))
    print(is_power_of_two(4))
    print(is_power_of_two(3))
