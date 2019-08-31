# -*- coding: utf-8 -*-


def reverseArray(arr):
    m = len(arr)/2

    if m == 0:
        return arr

    i = 0

    while i < m:
        arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
        i += 1
    return arr


if __name__ == '__main__':
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(reverseArray(arr))
