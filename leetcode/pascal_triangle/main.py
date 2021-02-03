"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""
from typing import List


def generate(numRows: int) -> List[List[int]]:
    pascal = []
    if numRows == 0:
        return pascal

    pascal = [[1]]
    last = [1]
    c = 1

    while True:
        if c < numRows:
            last = [1] + [last[i-1] + last[i] for i in range(c) if i > 0] + [1]
            pascal.append(last)
            c += 1
        else:
            break
    return pascal


if __name__ == '__main__':
    print(generate(4))
