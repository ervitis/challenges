# -*- coding: utf-8 -*-


def mini_max_sum(arr):
    s = [0] * len(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                s[i] += arr[j]
            j += 1
        i += 1

    return [min(s), max(s)]


def main():
    arr = list(map(int, '1 2 3 4 5'.rstrip().split()))

    print(mini_max_sum(arr))


if __name__ == '__main__':
    main()
