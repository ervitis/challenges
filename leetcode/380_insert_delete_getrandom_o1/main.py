"""
https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150
"""
import random


class RandomizedSet(object):

    def __init__(self):
        self._elems = []
        self._dict = {}

    def insert(self, val: int) -> bool:
        if val in self._dict:
            return False
        self._dict[val] = len(self._elems)
        self._elems.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._dict:
            return False
        # good trick, we are storing the index when we insert the element
        # so we can get the index and delete it
        last, i = self._elems[-1], self._dict[val]
        self._elems[i], self._dict[last] = last, i
        self._elems.pop()
        del self._dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self._elems)


def main():
    obj = RandomizedSet()
    param_1 = obj.insert(2)
    param_2 = obj.remove(3)
    param_3 = obj.getRandom()
    print(param_3, param_2, param_1)


if __name__ == '__main__':
    main()
