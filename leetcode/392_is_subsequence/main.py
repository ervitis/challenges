"""
https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150
"""


def is_subsequence(s: str, t: str) -> bool:
    i = j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


def main():
    print(is_subsequence('abc', 'ahbgdc'))
    print(is_subsequence('axc', 'ahbgdc'))


if __name__ == '__main__':
    main()
