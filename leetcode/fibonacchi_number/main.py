"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1
"""


def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n

    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(fib(2))
    print(fib(3))
    print(fib(4))
