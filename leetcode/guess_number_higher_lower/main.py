"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

    -1: The number I picked is lower than your guess (i.e. pick < num).
    1: The number I picked is higher than your guess (i.e. pick > num).
    0: The number I picked is equal to your guess (i.e. pick == num).
"""


def guess_number(n: int) -> int:
    low = 1
    high = n
    while low <= high:
        m = low + (high - low) // 2
        r = guess(m)
        if r == -1:
            high = m - 1
        elif r == 1:
            low = m + 1
        else:
            return m
    return -1


if __name__ == '__main__':
    print(guess_number(18))
