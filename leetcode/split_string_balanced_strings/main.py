"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.
"""


def balanced_string_split(s: str) -> int:
    if len(s) < 1:
        return 0

    st = {'L': 0, 'R': 0}
    co = 0
    for e in s:
        if e in st:
            st[e] += 1
        if st['L'] == st['R']:
            co += 1
            st['L'] = 0
            st['R'] = 0
    return co


if __name__ == '__main__':
    print(balanced_string_split('RLRRRLLRLL'))
    print(balanced_string_split('RLRRLLRLRL'))
