"""
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.
"""
from typing import List


def decompress_rle_list(nums: List[int]) -> List[int]:
    dl = []
    for i in range(0, len(nums), 2):
        freq, val = nums[i], nums[i + 1]
        while freq > 0:
            dl.append(val)
            freq -= 1
    return dl


if __name__ == '__main__':
    print(decompress_rle_list([1, 2, 3, 4]))
    print(decompress_rle_list([1, 1, 2, 3]))
