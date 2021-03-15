"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

    Choosing any x with 0 < x < N and N % x == 0.
    Replacing the number N on the chalkboard with N - x.

Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.
"""


def divisor_game(N: int) -> bool:
    p = True
    while N > 0:
        N -= 1
        p = not p
    return p


if __name__ == '__main__':
    print(divisor_game(2))
    print(divisor_game(3))
