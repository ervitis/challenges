"""
Given a binary string s without leading zeros, return true if s contains at most one contiguous segment of ones. Otherwise, return false.
"""


def check_ones_segment(s: str) -> bool:
    if '1' not in s:
        return False

    non_one_index = 0
    for k, c in enumerate(s):
        if c != '1':
            non_one_index = k
            break
        elif k == len(s) - 1:
            return True

    while non_one_index < len(s):
        if s[non_one_index] == '1':
            return False
        non_one_index += 1
    return True


if __name__ == '__main__':
    print(check_ones_segment('1001'))
    print(check_ones_segment('1'))
    print(check_ones_segment('10'))
    print(check_ones_segment('110'))
    print(check_ones_segment('110'))
    print(check_ones_segment('000000000000000'))
    print(check_ones_segment('000000011000000'))
