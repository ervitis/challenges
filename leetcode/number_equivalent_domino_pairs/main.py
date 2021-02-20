"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].
"""
from collections import Counter
from typing import List


def num_equiv_domino_pairs(dominoes: List[List[int]]) -> int:
    num = 0
    c = Counter()

    for domino in dominoes:
        key = min(domino[0], domino[1]) * 10 + max(domino[0], domino[1])
        num += c[key]
        c[key] += 1

    return num


if __name__ == '__main__':
    print(num_equiv_domino_pairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
