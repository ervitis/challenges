"""
Given a column title as appear in an Excel sheet, return its corresponding column number.
"""


def title_to_number(s: str) -> int:
    n, a = 0, 0
    for c in s[::-1]:
        n += (ord(c) - 64) * (26**a)
        a += 1
    return n


if __name__ == '__main__':
    print(title_to_number('A'))
    print(title_to_number('AB'))
    print(title_to_number('ZY'))
