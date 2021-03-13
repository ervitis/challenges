# -*- coding: utf-8 -*-

from collections import defaultdict, Counter


def is_anagram(s: str, t: str):
    if len(s) >= len(t):
        bd = s
        se = t
    else:
        bd = t
        se = s
    s1 = Counter(bd)

    for c in se:
        if c in s1:
            s1[c] = s1[c] - 1
    return all([e == 0 for e in s1.values()])


if __name__ == '__main__':
    print(is_anagram('anagram', 'nagaram'))
    print(is_anagram('rat', 'cat'))
    print(is_anagram('a', 'ab'))

