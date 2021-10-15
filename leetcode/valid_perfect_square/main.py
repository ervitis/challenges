"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.
"""


def is_perfect_square(num: int) -> bool:
    i = 1

    while i * i <= num:
        if num % i == 0 and num // i == i:
            return True
        i += 1
    return False


def main():
    print(is_perfect_square(16))
    print(is_perfect_square(14))
    print(is_perfect_square(2147483647))


if __name__ == '__main__':
    main()
