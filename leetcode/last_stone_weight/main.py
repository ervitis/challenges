"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

    If x == y, both stones are totally destroyed;
    If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
"""
from typing import List


def last_stone_weight(stones: List[int]) -> int:
    n = len(stones)
    for i in range(n):
        stones = sorted(stones)

        if n == 1:
            return stones[0]
        if n == 2:
            return stones[1] - stones[0]
        if stones[n-1] == stones[n-2]:
            stones.pop()
            stones.pop()
            n -= 2
        else:
            stones[n-2] = stones[n-1] - stones[n-2]
            stones.pop()
            n -= 1


if __name__ == '__main__':
    print(last_stone_weight([2, 7, 4, 1, 8, 1]))
    print(last_stone_weight([2, 2]))
    print(last_stone_weight([1]))
