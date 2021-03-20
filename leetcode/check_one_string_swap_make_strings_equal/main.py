"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false
"""
from collections import Counter


def are_almost_equal(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    if len(s1) != len(s2):
        return False

    c1 = Counter(s1)
    c2 = Counter(s2)
    for k, v in c1.items():
        if k not in c2.keys():
            return False
        if c2[k] != v:
            return False

    for i in range(len(s1)-1):
        t = list(s1)
        for j in range(len(t)-1, i, -1):
            if t[i] == t[j]:
                continue
            t[i], t[j] = t[j], t[i]
            if ''.join(t) == s2:
                return True
            else:
                t[i], t[j] = t[j], t[i]
    return False


if __name__ == '__main__':
    print(are_almost_equal('bank', 'kanb'))
    print(are_almost_equal('abcd', 'dcba'))
    print(are_almost_equal('attack', 'defend'))
    print(are_almost_equal('kelb', 'kelb'))
    print(are_almost_equal('holaamigo', 'hmlaaoigo'))
    print(are_almost_equal('siyolsdcjthwsiplccjbuceoxmpjgrauocx', 'siyolsdcjthwsiplccpbuceoxmjjgrauocx'))
