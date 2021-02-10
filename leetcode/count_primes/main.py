"""
Count the number of prime numbers less than a non-negative number, n
"""


def count_primes(n: int) -> int:
    if n <= 2:
        return 0

    prime = [True] * n
    prime[:2] = [False] * 2
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            prime[i * i:n:i] = [False] * len(prime[i * i:n:i])

    return sum(prime)


if __name__ == '__main__':
    print(count_primes(10))
    print(count_primes(0))
    print(count_primes(1))
    print(count_primes(2))
    print(count_primes(5000000))
