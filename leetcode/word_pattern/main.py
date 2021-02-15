"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s
"""


def word_pattern(pattern: str, s: str) -> bool:
    if len(pattern) < 1:
        return False
    if len(s) < 1:
        return False
    if len(pattern) != len(s.split(' ')):
        return False

    s = s.split(' ')
    wp = {}
    sd = {}

    for i in range(len(pattern)):
        if pattern[i] not in wp:
            wp[pattern[i]] = s[i]
        else:
            if wp[pattern[i]] == s[i]:
                continue
            else:
                return False

        if s[i] in sd:
            if sd[s[i]] != pattern[i]:
                return False
        else:
            sd[s[i]] = pattern[i]
    return True


if __name__ == '__main__':
    print(word_pattern("abba", "dog cat cat dog"))
    print(word_pattern("abba", "dog cat cat fish"))
