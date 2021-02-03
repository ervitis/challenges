"""
Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.
"""
from typing import List


T = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


def get_row(rowIndex: int) -> List[int]:
    last = [1]
    if rowIndex == 0:
        return last

    c = 1
    line = 0

    while True:
        if line < rowIndex:
            last = [1] + [last[i - 1] + last[i] for i in range(c) if i > 0] + [1]
            c += 1
            line += 1
        else:
            break
    return last


if __name__ == '__main__':
    print(get_row(0))
