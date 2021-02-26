"""
Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
"""


def number_of_steps(num: int) -> int:
    c = 0
    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        c += 1
    return c


if __name__ == '__main__':
    print(number_of_steps(14))
    print(number_of_steps(8))
