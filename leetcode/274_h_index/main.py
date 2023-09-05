"""
https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


def h_index(citations: List[int]) -> int:
    m = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            m = i + 1
    return m


def main():
    print(h_index([3, 0, 6, 1, 5]))
    print(h_index([1, 3, 1]))


if __name__ == '__main__':
    main()
