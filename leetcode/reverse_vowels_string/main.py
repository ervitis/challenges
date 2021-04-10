"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
"""


def reverse_vowels(s: str) -> str:
    i, j = len(s) - 1, 0
    s = list(s)
    while i > j:
        if s[i] in 'aeiouAEIOU':
            while s[j] not in 'aeiouAEIOU':
                j += 1
            else:
                s[i], s[j] = s[j], s[i]
                j += 1
        i -= 1
    return ''.join(s)


if __name__ == '__main__':
    print(reverse_vowels('hello'))
    print(reverse_vowels('leetcode'))
    print(reverse_vowels('aA'))
