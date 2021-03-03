"""
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.
"""
from typing import List


def odd_cells(n: int, m: int, indices: List[List[int]]) -> int:
    mat = [[0] * m for i in range(n)]
    for r, c in indices:
        for i in range(m):
            mat[r][i] += 1
        for i in range(n):
            mat[i][c] += 1
    return sum([1 for r in mat for c in r if c % 2 != 0])


if __name__ == '__main__':
    print(odd_cells(2, 3, [[0, 1], [1, 1]]))
    print(odd_cells(2, 2, [[1, 1], [0, 0]]))
