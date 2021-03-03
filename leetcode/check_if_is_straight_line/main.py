"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
"""
import sys
from typing import List


def check_straight_line(coordinates: List[List[int]]) -> bool:
    if len(coordinates) < 2:
        return True

    (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
    for x, y in coordinates:
        if (y - y1) * (x1 - x0) != (y1 - y0) * (x - x1):
            return False
    return True


if __name__ == '__main__':
    print(check_straight_line([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
    print(check_straight_line([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
    print(check_straight_line([[0, 0], [0, 1], [0, -1]]))
    print(check_straight_line([[2, 4], [2, 5], [2, 8]]))
