"""
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
"""
from collections import defaultdict
from typing import List


def count_consistent_strings(allowed: str, words: List[str]) -> int:
    c = 0
    sa = set(allowed)
    for word in words:
        if all(w in sa for w in word):
            c += 1
    return c


if __name__ == '__main__':
    print(count_consistent_strings('ab', ["ad", "bd", "aaab", "baa", "badab"]))
    print(count_consistent_strings('abc', ["a", "b", "c", "ab", "ac", "bc", "abc"]))
