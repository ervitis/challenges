"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
"""


def convert_to_title(n: int) -> str:
    t = ''

    while n > 0:
        r = n % 26
        c = chr(ord("A") + r - 1) if r > 0 else "Z"
        t = c + t
        n = n // 26 if r > 0 else n // 26 - 1
    return t


if __name__ == '__main__':
    print(convert_to_title(1))
    print(convert_to_title(2))
    print(convert_to_title(28))
    print(convert_to_title(701))
