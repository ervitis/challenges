"""
https://leetcode.com/problems/3sum/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    res = []

    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            t = nums[i] + nums[l] + nums[r]
            if t < 0:
                l += 1
            elif t > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res


def main():
    print(three_sum([-1, 0, 1, 2, -1, -4]))
    print(three_sum([0, 1, 1]))
    print(three_sum([0, 0, 0]))


if __name__ == '__main__':
    main()
