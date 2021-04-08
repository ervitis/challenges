"""
Write a function that reverses a string. The input string is given as an array of characters s.
"""
from typing import List


class Solution:
    def reverse_string(self, s: List[str]) -> None:
        s.reverse()


if __name__ == '__main__':
    print(Solution().reverse_string(['h', 'e']))
