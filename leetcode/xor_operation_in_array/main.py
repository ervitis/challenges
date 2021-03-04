"""
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
"""


def xor_operation(n: int, start: int) -> int:
    nums = [i for i in range(start, start+n*2, 2)]
    x = nums[0]
    for n in nums[1:]:
        x ^= n
    return x


if __name__ == '__main__':
    print(xor_operation(5, 0))
    print(xor_operation(4, 3))
    print(xor_operation(1, 7))
    print(xor_operation(10, 5))
