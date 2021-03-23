"""
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.
"""
from typing import List


def max_count(m: int, n: int, ops: List[List[int]]) -> int:
    for op in ops:
        m = min(m, op[0])
        n = min(n, op[1])
    return m * n


if __name__ == '__main__':
    print(max_count(3, 3, [[2, 2], [3, 3]]))
    print(max_count(3, 3, [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]]))
    print(max_count(3, 3, []))
    print(max_count(3000, 3000, []))
