"""
You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

abc
bce
cae

You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.
"""
from typing import List


def min_deletion_size(strs: List[str]) -> int:
    dc = 0

    for i in range(len(strs[0])):
        for j in range(len(strs)-1):
            if ord(strs[j][i]) > ord(strs[j + 1][i]):
                dc += 1
                break

    return dc


if __name__ == '__main__':
    print(min_deletion_size(["cba", "daf", "ghi"]))
    print(min_deletion_size(["a", "b"]))
    print(min_deletion_size(["zyx", "wvu", "tsr"]))
    print(min_deletion_size(["rrjk", "furt", "guzm"]))
