"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
"""
from typing import List


def array_strings_are_equal(word1: List[str], word2: List[str]) -> bool:
    a, b = '', ''
    for w in word1:
        a += w

    for w in word2:
        b += w
        if b != a[:len(b)]:
            return False
    return a == b


if __name__ == '__main__':
    print(array_strings_are_equal(["ab", "c"], ["a", "bc"]))
    print(array_strings_are_equal(["abc", "d", "defg"], ["abcddefg"]))
    print(array_strings_are_equal(["abc", "d", "defg"], ["abcddef"]))
