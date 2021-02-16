"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
"""
from typing import List


def di_string_match(S: str) -> List[int]:
    arr = [i for i in range(len(S)+1)]

    return [arr.pop(0) if e == 'I' else arr.pop(-1) for e in S] + arr


if __name__ == '__main__':
    print(di_string_match('IDID'))
    print(di_string_match('IIIIII'))
    print(di_string_match('IIDIID'))
    print(di_string_match('DDI'))
