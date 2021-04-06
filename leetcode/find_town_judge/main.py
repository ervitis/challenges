"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
"""
from typing import List


def find_judge(N: int, trust: List[List[int]]) -> int:
    d = {e: set() for e in range(1, N + 1)}

    for p1, p2 in trust:
        if p1 in d:
            d.pop(p1)
        if p2 in d:
            d[p2].add(p1)

    for k, v in d.items():
        if len(v) == N - 1:
            return k
    return -1


if __name__ == '__main__':
    print(find_judge(2, [[1, 2]]))
    print(find_judge(3, [[1, 3], [2, 3]]))
    print(find_judge(3, [[1, 3], [2, 3], [3, 1]]))
    print(find_judge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
    print(find_judge(3, [[1, 2], [2, 3]]))
