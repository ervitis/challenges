# -*- coding: utf-8 -*-

import random
import time
from copy import deepcopy

from algorithms import Selection, Insertion, MergeSort, SortIface, QuickSort, HeapSort

MIN_VALUE = -1000
MAX_VALUE = 1000


class SortAlgorithms(object):

    def __init__(self):
        self._data = [random.randrange(MIN_VALUE, MAX_VALUE) for _ in range(0, 1000)]
        print(f'My data is {self._data}')

    def execute_with_alg(self, alg: SortIface):
        t_begin = int(round(time.time() * 1000))
        print(alg.sort(deepcopy(self._data)))
        t_end = int(round(time.time() * 1000))
        print(f'Finished {alg.name} in {t_end - t_begin} milliseconds')


def main():
    algs = [
        Selection(),
        Insertion(),
        MergeSort(),
        QuickSort(),
        HeapSort(),
    ]

    sort_algorithms = SortAlgorithms()

    for alg in algs:
        sort_algorithms.execute_with_alg(alg)


if __name__ == '__main__':
    main()
