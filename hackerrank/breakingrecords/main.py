# -*- coding: utf-8 -*-


def breaking_records(scores):
    bhs, bls = 0, 0

    if len(scores) == 0:
        return 0, 0

    hs = ls = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > hs:
            hs = scores[i]
            bhs += 1
        elif scores[i] < ls:
            ls = scores[i]
            bls += 1
    return bhs, bls


def main():
    scores = list(map(int, '10 5 20 20 4 5 2 25 1'.rstrip().split()))
    result = breaking_records(scores)
    print(result)

    scores = list(map(int, '3 4 21 36 10 28 35 5 24 42'.rstrip().split()))
    result = breaking_records(scores)
    print(result)


if __name__ == '__main__':
    main()
