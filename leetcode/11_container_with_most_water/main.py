"""
https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


def max_area(height: List[int]) -> int:
    ma = 1
    l = 0
    r = len(height) - 1
    h = max(height)

    while l < r:
        ma = max(ma, (min(height[l], height[r])) * (r - l))

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
        if (r - l) * h <= ma:
            break
    return ma


def main():
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(max_area([1, 2]))


if __name__ == '__main__':
    main()
