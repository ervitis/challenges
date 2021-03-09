"""
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""
from typing import List


def largest_altitude(gain: List[int]) -> int:
    a = [0] * (len(gain) + 1)
    ma = 0
    for k, v in enumerate(gain):
        a[k+1] = v + a[k]
        if a[k+1] > ma:
            ma = a[k+1]
    return ma


if __name__ == '__main__':
    print(largest_altitude([-5, 1, 5, 0, -7]))
    print(largest_altitude([-4, -3, -2, -1, 4, 3, 2]))
