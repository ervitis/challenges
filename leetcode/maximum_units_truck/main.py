"""
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

    numberOfBoxesi is the number of boxes of type i.
    numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
"""
from typing import List


def maximum_units(boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    res = 0
    i = 0
    while truckSize and i < len(boxTypes):
        left, units = boxTypes[i]
        if truckSize >= left:
            res += units * left
            truckSize -= left
            i += 1
        else:

            res += units * truckSize
            truckSize = 0

    return res


if __name__ == '__main__':
    print(maximum_units([[1, 3], [2, 2], [3, 1]], 4))
    print(maximum_units([[5, 10], [2, 5], [4, 7], [3, 9]], 10))
