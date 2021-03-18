"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
"""


def valid_palindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            a = s[i+1:j+1]
            b = s[i:j]
            if a == a[::-1] or b == b[::-1]:
                return True
            else:
                return False
    return True


if __name__ == '__main__':
    print(valid_palindrome('aba'))
    print(valid_palindrome('abca'))
    print(valid_palindrome('bcagcfacb'))
