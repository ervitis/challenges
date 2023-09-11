"""
https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150
"""


def int_to_roman(num: int) -> str:
    symbols = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]
    r = ''
    for s, v in symbols:
        c = num // v
        r += s * c
        num %= v
    return r


def main():
    print(int_to_roman(3))
    print(int_to_roman(1994))


if __name__ == '__main__':
    main()
