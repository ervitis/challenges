"""
https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


def is_valid_sudoku(board: List[List[str]]) -> bool:
    def is_unique(nums: List[str]) -> bool:
        nums = [n for n in nums if n != '.']
        return len(nums) == len(set(nums))
    for i in range(9):
        if not is_unique(board[i]):
            return False
    for i in range(9):
        if not is_unique([board[j][i] for j in range(9)]):
            return False
    for i in range(3):
        for j in range(3):
            if not is_unique([board[f][c] for c in range(3*j, 3*j+3) for f in range(3*i, 3*i+3)]):
                return False
    return True


def main():
    print(is_valid_sudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                              , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                              , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                              , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                              , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                              , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                              , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                              , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                              , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))


if __name__ == '__main__':
    main()
