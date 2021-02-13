"""
Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
"""
from collections import defaultdict


def buddy_strings(A: str, B: str) -> bool:
    if len(A) != len(B):
        return False
    if A == B and len(A) > len(set(A)):
        return True
    if A == B:
        return False

    da, db = [], []

    for i in range(len(A)):
        if A[i] != B[i]:
            da.append(A[i])
            db.append(B[i])
    if len(da) > 2:
        return False
    if len(da) == 2 and da == db[::-1]:
        return True


if __name__ == '__main__':
    print(buddy_strings("ab", "ba"))
    print(buddy_strings("ab", "ab"))
    print(buddy_strings("aa", "aa"))
    print(buddy_strings("aaaaaaabc", "aaaaaaacb"))
    print(buddy_strings("", "ab"))
