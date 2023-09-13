"""
https://leetcode.com/problems/zigzag-conversion/?envType=study-plan-v2&envId=top-interview-150
"""


def convert(s: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(s):
        return s

    table = ['' for _ in range(num_rows)]
    cycle = 2 * num_rows - 2

    for i in range(len(s)):
        pos = i % cycle
        row = min(pos, cycle - pos)
        table[row] += s[i]
    return ''.join(table)


def main():
    print(convert('PAYPALISHIRING', 3))
    print(convert('PAYPALISHIRING', 4))
    print(convert('A', 1))


if __name__ == '__main__':
    main()
