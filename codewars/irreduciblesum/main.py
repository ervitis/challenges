# -*- coding: utf-8 -*-
from functools import reduce
from math import gcd


def sum_rationals(lst):
    if lst is None or len(lst) == 0:
        return None

    def lcm(ns):
        return reduce(lambda a, b: a*b // gcd(a, b), ns)

    cl = []
    for e in lst:
        d = gcd(e[0], e[1])
        cl.append([e[0] // d, e[1] // d])

    lc = lcm([d[1] for d in cl])

    s = 0
    for d in cl:
        t = lc // d[1]
        t = t * d[0]
        s += t

    if s % lc == 0:
        return s // lc

    return [s, lc]


def main():
    print(sum_rationals([[45885, 34060]]))


if __name__ == '__main__':
    main()
