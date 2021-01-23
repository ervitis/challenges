# -*- coding: utf-8 -*-

import random
import sys
import copy
import os


class Minesweeper(object):
    """
    m x n and probability p of a mine to appear
    """
    def __init__(self, n, m, p):
        self.__n = 3
        self.__m = 3
        self.__bombs = [[0, 0, 0], [0, -1, -1], [-1, -1, 0]]  # [[-1 if random.random() < p else 0 for _ in range(n)] for _ in range(m)]
        self.__board = copy.deepcopy(self.__bombs)
        self.__free = self.__n * self.__m
        self.__number_bombs = 0
        self._prepare_board()
        self._print_board()
        self._neighbours()
        self.__over = False

    def _neighbours(self):
        if self.__n < 2 and self.__m < 2:
            return

        for i in range(self.__n):
            for j in range(self.__m):

                if self.__bombs[i][j] == -1:
                    self.__number_bombs += 1
                    continue

                # up left
                if i > 0 and j > 0 and self.__bombs[i-1][j-1] == -1:
                    self.__bombs[i][j] += 1
                # up
                if i > 0 and self.__bombs[i-1][j] == -1:
                    self.__bombs[i][j] += 1
                # up right
                if i > 0 and j < self.__m - 1 and self.__bombs[i-1][j+1] == -1:
                    self.__bombs[i][j] += 1
                # left
                if j > 0 and self.__bombs[i][j-1] == -1:
                    self.__bombs[i][j] += 1
                # right
                if j < self.__m - 1 and self.__bombs[i][j+1] == -1:
                    self.__bombs[i][j] += 1
                # down left
                if i < self.__n - 1 and j > 0 and self.__bombs[i+1][j-1] == -1:
                    self.__bombs[i][j] += 1
                # down
                if i < self.__n - 1 and self.__bombs[i+1][j] == -1:
                    self.__bombs[i][j] += 1
                # down right
                if i < self.__n - 1 and j < self.__m - 1 and self.__bombs[i+1][j+1] == -1:
                    self.__bombs[i][j] += 1

    def _print_board(self):
        for row in self.__board:
            for col in row:
                print(col, sep=' ', end=' ')
            print()

    def _print_bombs(self):
        for row in self.__bombs:
            for col in row:
                print(col, sep=' ', end=' ')
            print()

    def _get_coordinate(self):
        while 1:
            data = input('\nWrite the coordinates separated by white space (eg. 3 4): ').split(' ')
            try:
                if len(data) == 2 and 0 <= int(data[0]) <= self.__n and 0 <= int(data[1]) <= self.__m:
                    return int(data[0]), int(data[1])
            except Exception:
                pass

    def _prepare_board(self):
        for row in range(self.__n):
            for col in range(self.__m):
                if self.__board[row][col] == -1:
                    self.__board[row][col] = '*'
                else:
                    self.__board[row][col] = '.'

    def init(self):
        def clear():
            os.system('clear')

        while self.__over is False:
            x, y = self._get_coordinate()
            if x >= self.__n or y >= self.__m:
                continue
            if self.__bombs[x][y] == -1:
                self.__board[x][y] = 'X'
                print('BOOOOOOOOOOOOOOOOOOM')
                self.__over = True
            else:
                self.__board[x][y] = self.__bombs[x][y]
                if self.__number_bombs - ((self.__n * self.__m) - self.__free) <= 0:
                    print('YOU WIN!!!')
                    self.__over = True
                self.__free -= 1

            clear()
            self._print_board()


def main():
    if len(sys.argv) != 4:
        m = n = 5
        p = 0.3
    else:
        m = int(sys.argv[1]) or 5
        n = int(sys.argv[2]) or 5
        p = float(sys.argv[3]) or 0.6

    if p > 0.99999:
        p = 0.6

    minesweeper = Minesweeper(n, m, p)

    minesweeper.init()


if __name__ == '__main__':
    main()
