"""
https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[int]]:
    grs = defaultdict(list)
    for s in strs:
        ss = ''.join(sorted(s))
        grs[ss].append(s)
    return list(grs.values())


def main():
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == '__main__':
    main()
