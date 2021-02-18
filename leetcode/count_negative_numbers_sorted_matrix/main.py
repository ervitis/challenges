"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid
"""
from typing import List


def count_negatives(grid: List[List[int]]) -> int:
    count = 0
    m = len(grid)
    r = m - 1
    n = len(grid[0])
    c = 0

    while r >= 0 and c < n:
        if grid[r][c] < 0:
            r -= 1
            count += n - c
        else:
            c += 1
    return count


if __name__ == '__main__':
    print(count_negatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
    print(count_negatives([[3, 2], [1, 0]]))
