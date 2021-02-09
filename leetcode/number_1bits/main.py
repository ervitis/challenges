"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
"""


def hamming_weight(n: int) -> int:
    return bin(n).count('1')


if __name__ == '__main__':
    print(hamming_weight(int('{0:032b}'.format(111001011110000010100101000000))))
