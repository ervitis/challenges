"""
https://leetcode.com/problems/spiral-matrix/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    res = []
    while top <= bottom and left <= right:
        for i in range(left, right+1):
            res.append(matrix[top][i])
        top += 1

        for i in range(top, bottom+1):
            res.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
    return res


def main():
    print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


if __name__ == '__main__':
    main()
