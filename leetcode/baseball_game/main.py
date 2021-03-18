"""
You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

    An integer x - Record a new score of x.
    "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
    "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
    "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.

Return the sum of all the scores on the record.
"""
from typing import List


def cal_points(ops: List[str]) -> int:
    r = []
    i = 0
    for op in ops:
        if op == 'C':
            r.pop(i - 1)
            i -= 1
        elif op == 'D':
            if i > 0:
                d = r[i - 1] * 2
            else:
                d = 0
            r.append(d)
            i += 1
        elif op == '+':
            if i > 0:
                d = r[i-1] + r[i-2]
            else:
                d = r[i]
            r.append(d)
            i += 1
        else:
            d = int(op)
            r.append(d)
            i += 1
    return sum(r)


if __name__ == '__main__':
    print(cal_points(["5", "2", "C", "D", "+"]))
    print(cal_points(["5", "-2", "4", "C", "D", "9", "+", "+"]))
    print(cal_points(["1"]))
