"""
Reverse bits of a given 32 bits unsigned integer.
"""


def reverse_bits(n: int) -> int:
    r = 0

    for _ in range(32):
        r = r << 1
        r += n & 1
        n = n >> 1

    return r


if __name__ == '__main__':
    print(reverse_bits(int('{0:032b}'.format(111001011110000010100101000000))))
