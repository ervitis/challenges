"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""
import re


def is_palindrome(s: str) -> bool:
    i = 0
    s = re.sub(r'[\W_-]+', '', s).lower()
    ln = len(s)

    while i < ln // 2:
        if s[i] != s[ln - 1 - i]:
            return False
        i += 1
    return True


if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("race a car"))
    print(is_palindrome(""))
    print(is_palindrome("ab_a"))
