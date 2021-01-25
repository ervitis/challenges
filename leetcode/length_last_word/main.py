"""
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.
"""


def length_of_last_word(s: str) -> int:
    max_length = 0
    s = s.strip()

    for i in range(len(s)):
        if s[i] == ' ':
            max_length = 0
        else:
            max_length += 1
    return max_length


if __name__ == '__main__':
    print(length_of_last_word("Hello World"))
    print(length_of_last_word(" "))
