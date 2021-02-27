"""
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.
"""
from typing import List


def restore_string(s: str, indices: List[int]) -> str:
    if len(s) != len(indices):
        return ''

    sf = [''] * len(s)
    for k, v in enumerate(indices):
        sf[v] = s[k]
    return ''.join(sf)


if __name__ == '__main__':
    print(restore_string('aiohn', [3, 1, 4, 2, 0]))
    print(restore_string('codeleet', [4, 5, 6, 7, 0, 2, 1, 3]))
