"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1
"""


def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n

    return fib(n-1) + fib(n-2)


def fib2(n: int) -> int:
    r = [0 for i in range(n+1)]
    r[0] = 0
    if n >= 1:
        r[1] = 1
        for e in range(2, n+1):
            r[e] = r[e-1] + r[e-2]
    return r[-1]


if __name__ == '__main__':
    print(fib(2))
    print(fib(3))
    print(fib(4))
    print(fib2(2))
    print(fib2(3))
    print(fib2(4))
