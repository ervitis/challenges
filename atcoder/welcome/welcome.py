# -*- coding: utf-8 -*-


def main():
    def addition(n, m, o):
        return n + m + o

    a = int(input())
    b, c = map(int, input().split())
    s = input()

    print('{} {}'.format(addition(a, b, c), s))


if __name__ == '__main__':
    main()
