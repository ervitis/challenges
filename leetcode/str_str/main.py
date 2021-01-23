"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


def str_str(haystack: str, needle: str) -> int:
    if len(needle) > len(haystack):
        return -1
    if len(haystack) == 0 or len(needle) == 0:
        return 0
    if len(haystack) == len(needle):
        return 0 if haystack == needle else -1
    i = 0
    n = len(needle)
    while i < len(haystack):
        d = haystack[i:i+n]
        if d == needle:
            return i
        i += 1
    return -1


if __name__ == '__main__':
    print(str_str("hello", "ll"))
    print(str_str("aaaaa", "bba"))
    print(str_str("", ""))
    print(str_str("a", "a"))
    print(str_str("abc", "c"))
