"""
You are given an integer n, the number of teams in a tournament that has strange rules:

    If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
    If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.

Return the number of matches played in the tournament until a winner is decided.
"""


def number_of_matches(n: int) -> int:
    if n < 2:
        return 0

    c = 0
    while n > 1:
        if n % 2 != 0:
            m = (n - 1) // 2
            n = (n - 1) // 2 + 1
        else:
            m = n // 2
            n //= 2
        c += m
    return c


if __name__ == '__main__':
    print(number_of_matches(7))
    print(number_of_matches(14))
    print(number_of_matches(1))
    print(number_of_matches(0))
    print(number_of_matches(2))
