# -*- coding: utf-8 -*-


def compare_triplets(a, b):
    points = [0, 0]
    for p1, p2 in zip(a, b):
        if p1 < p2:
            points[1] += 1
        elif p1 > p2:
            points[0] += 1
    return points


def main():
    a = list(map(int, '17 28 30'.rstrip().split()))

    b = list(map(int, '99 16 8'.rstrip().split()))

    print(compare_triplets(a, b))


if __name__ == '__main__':
    main()
