"""
https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    start = total = st = 0
    for i in range(len(gas)):
        st += gas[i] - cost[i]
        if st < 0:
            start = i + 1
            total += st
            st = 0
    return start if total + st >= 0 else -1


def main():
    print(can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(can_complete_circuit([2, 3, 4], [3, 4, 3]))


if __name__ == '__main__':
    main()
