"""

"""
from typing import List


def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            n -= 1
    return n <= 0


if __name__ == '__main__':
    print(can_place_flowers([1, 0, 0, 0, 1], 1))
    print(can_place_flowers([1, 0, 0, 0, 1], 2))
    print(can_place_flowers([1, 0], 1))
    print(can_place_flowers([1, 0, 1], 1))
    print(can_place_flowers([1, 0, 0, 1], 1))
    print(can_place_flowers([1, 0, 1, 0, 1, 0], 1))
    print(can_place_flowers([1, 0, 1, 0, 1, 0, 0], 1))
