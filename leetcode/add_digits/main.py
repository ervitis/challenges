"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
"""


def add_digits(num: int) -> int:
    return 0 if num == 0 else 9 if num % 9 == 0 else num % 9


if __name__ == '__main__':
    print(add_digits(38))
    print(add_digits(9))
    print(add_digits(3))
    print(add_digits(18))
