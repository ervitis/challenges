"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    hash_map = dict()
    chrs = set()

    for i in range(0, len(s)):
        sc = s[i]
        tc = t[i]

        if sc in hash_map:
            if hash_map[sc] != tc:
                return False
        else:
            if tc in chrs:
                return False
        hash_map[sc] = tc
        chrs.add(tc)
    return True


if __name__ == '__main__':
    print(is_isomorphic('egg', 'add'))
    print(is_isomorphic('foo', 'bar'))
    print(is_isomorphic('paper', 'title'))
    print(is_isomorphic('badc', 'baba'))
