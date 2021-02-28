"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""


def substract_product_and_sum(n: int) -> int:
    s, m = 0, 1
    while n > 0:
        t = n % 10
        s += t
        m *= t
        n //= 10
    return m - s


if __name__ == '__main__':
    print(substract_product_and_sum(234))
    print(substract_product_and_sum(4421))
