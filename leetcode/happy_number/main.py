"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""


def is_happy(n: int) -> bool:
    ocurrences = set()
    curr = n

    while curr != 1:
        curr = sum([int(x)**2 for x in list(str(n))])
        if curr in ocurrences:
            return False
        ocurrences.add(curr)
        n = curr
    return True


if __name__ == '__main__':
    print(is_happy(19))
    print(is_happy(2))
