# -*- coding: utf-8 -*-


def birthday_cake_candles(ar):
    m = max(ar)
    c = 0
    for n in ar:
        if n == m:
            c += 1
    return c


def main():
    ar = list(map(int, '3 2 1 3'.rstrip().split()))
    print(birthday_cake_candles(ar))


if __name__ == '__main__':
    main()
