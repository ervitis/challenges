"""
You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.

You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.

Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.

Return the number of rectangles that can make a square with a side length of maxLen.
"""
from typing import List


def count_good_rectangles(rectangles: List[List[int]]) -> int:
    sq = {}
    for r in rectangles:
        m = min(r)
        if m not in sq:
            sq[m] = 1
        else:
            sq[m] += 1
    if len(sq) == 0:
        return 0

    m = 0
    for k, v in sq.items():
        if k > m:
            m = k
    return sq[m]


if __name__ == '__main__':
    print(count_good_rectangles([[5, 8], [3, 9], [5, 12], [16, 5]]))
    print(count_good_rectangles([[2, 3], [3, 7], [4, 3], [3, 7]]))
