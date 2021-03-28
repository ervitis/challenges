"""
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

    Rank is an integer starting from 1.
    The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
    Rank should be as small as possible.

"""
from typing import List


def array_rank_transform(arr: List[int]) -> List[int]:
    s = sorted(set(arr))
    s = dict(zip(s, range(1, len(s) + 1)))
    for k, v in enumerate(arr):
        arr[k] = s[v]
    return arr


if __name__ == '__main__':
    print(array_rank_transform([40, 10, 20, 30]))
    print(array_rank_transform([37, 12, 28, 9, 100, 56, 80, 5, 12]))
