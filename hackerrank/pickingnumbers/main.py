# -*- coding: utf-8 -*-

from collections import defaultdict


def pickingNumbers(a):
    d = defaultdict(int)
    r = 0

    for v in a:
        d[v] += 1
        r = max(r, d[v]+d[v+1], d[v]+d[v-1])

    return r


if __name__ == '__main__':
    # n = int(input().strip())

    a = list(map(int, '1 1 2 2 4 4 5 5 5'.rstrip().split()))

    result = pickingNumbers(a)

    print(result)
