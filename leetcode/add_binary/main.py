"""
Given two binary strings a and b, return their sum as a binary string.
"""


def add_binary(a: str, b: str) -> str:
    ln = max(len(a), len(b))
    a = a.zfill(ln)
    b = b.zfill(ln)

    r = ''
    acc = 0
    for i in range(ln - 1, -1, -1):
        s = int(a[i]) + int(b[i]) + acc
        acc = s // 2
        v = s % 2
        r = str(v) + r
    if acc > 0:
        r = str(acc) + r
    return r


if __name__ == '__main__':
    print(add_binary('11', '1'))
    print(add_binary('1010', '1011'))
    print(add_binary('1111', '1011'))
    print(add_binary('1011', '10101011'))
    print(add_binary('1010101010', '0101010101'))
