"""
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.
"""
from math import sqrt
from typing import List


def is_boomerang(points: List[List[int]]) -> bool:
    return abs((points[0][0] * (points[1][1] - points[2][1]) + points[1][0] * (points[2][1] - points[0][1]) + points[2][0] * (points[0][1] - points[1][1])) / 2) > 0


if __name__ == '__main__':
    print(is_boomerang([[1, 1], [2, 3], [3, 2]]))
    print(is_boomerang([[1, 1], [2, 2], [3, 3]]))
    print(is_boomerang([[0, 0], [1, 0], [2, 2]]))
    print(is_boomerang([[0, 0], [2, 1], [2, 1]]))
