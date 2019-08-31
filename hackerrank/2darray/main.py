# -*- coding: utf-8 -*-


HOURGLASSCOORDINATES = [(-1, -1), (-1, 0), (-1, 1), (0, 0), (1, -1), (1, 0), (1, 1)]


def hourglassSum(arr):
    i = 1
    k = 0

    s = [0] * 16

    while i < len(arr) - 1:
        j = 1
        while j < len(arr[i]) - 1:
            s[k] += sum(arr[i + hc[0]][j + hc[1]] for hc in HOURGLASSCOORDINATES)

            j += 1
            k += 1
        i += 1
    s.sort(reverse=True)
    return s[0]


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
