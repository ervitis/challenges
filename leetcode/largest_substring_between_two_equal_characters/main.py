"""
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.
"""


def max_length_between_equal_characters(s: str) -> int:
    ma = {}
    for i in range(len(s)):
        f = [j for j, c in enumerate(s) if c == s[i]]
        if s[i] not in ma and len(f) > 1:
            ma[s[i]] = f
    m = 0
    for v in ma.values():
        if m < v[len(v)-1] - v[0]:
            m = v[len(v)-1] - v[0]
    return m - 1


if __name__ == '__main__':
    print(max_length_between_equal_characters('aa'))
    print(max_length_between_equal_characters('abca'))
    print(max_length_between_equal_characters('cbzxy'))
    print(max_length_between_equal_characters('cabbac'))
    print(max_length_between_equal_characters('ojdncpvyneq'))
    print(max_length_between_equal_characters('mgntdygtxrvxjnwksqhxuxtrv'))
