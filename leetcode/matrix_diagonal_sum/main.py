"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
"""
from typing import List


def diagonal_sum(mat: List[List[int]]) -> int:
    n = len(mat)
    return sum([mat[i][j] for i in range(n) for j in range(n) if i == j or j == n - i - 1])


if __name__ == '__main__':
    print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(diagonal_sum([[5]]))
    print(diagonal_sum([[1, 1, 1, 1],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1]]))
