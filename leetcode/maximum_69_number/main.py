"""
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""


def maximum_69_number(num: int) -> int:
    ns = list(str(num))

    if '6' not in ns:
        return num

    for i in range(len(ns)):
        if ns[i] == '6':
            ns[i] = '9'
            break
    return int(''.join(ns))


if __name__ == '__main__':
    print(maximum_69_number(9969))
    print(maximum_69_number(9996))
    print(maximum_69_number(9999))
    print(maximum_69_number(99969969))
