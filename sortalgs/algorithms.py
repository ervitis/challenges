# -*- coding: utf-8 -*-
from typing import List

import sys
sys.setrecursionlimit(1000000)


class SortIface(object):

    def __init__(self, name):
        self.__name = name

    def sort(self, data: List[int]):
        raise NotImplementedError

    @property
    def name(self):
        return self.__name


class Selection(SortIface):
    def __init__(self):
        super(Selection, self).__init__('selection')

    def sort(self, data: List[int]):
        for i in range(len(data)):
            min_idx = i
            for j in range(i+1, len(data)):
                if data[min_idx] > data[j]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]

        return data


class Insertion(SortIface):
    def sort(self, data: List[int]):
        for i in range(1, len(data)):
            k = data[i]

            j = i - 1
            while j >= 0 and k < data[j]:
                data[j+1] = data[j]
                j -= 1
            data[j+1] = k
        return data

    def __init__(self):
        super(Insertion, self).__init__('insertion')


class MergeSort(SortIface):

    def __init__(self):
        super(MergeSort, self).__init__('mergesort')

    def sort(self, data: List[int]):
        if len(data) > 1:
            mid = len(data) // 2

            left = data[mid:]
            right = data[:mid]

            self.sort(left)
            self.sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    data[k] = left[i]
                    i += 1
                else:
                    data[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                data[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                data[k] = right[j]
                j += 1
                k += 1
        return data


class QuickSort(SortIface):

    def __init__(self):
        super(QuickSort, self).__init__('quicksort')

    def sort(self, data: List[int]):
        def partition(arr: List[int], low: int, high: int):
            i = low - 1
            pivot = arr[high]

            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return i + 1

        def quicksort(arr: List[int], low: int, high: int):
            if low < high:
                pivot = partition(arr, low, high)

                quicksort(arr, low, pivot-1)
                quicksort(arr, pivot+1, high)

        quicksort(data, 0, len(data)-1)
        return data


class HeapSort(SortIface):

    def __init__(self):
        super(HeapSort, self).__init__('heapsort')

    def sort(self, data: List[int]):
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[largest] < arr[l]:
                largest = l
            if r < n and arr[largest] < arr[r]:
                largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        def heap_sort(arr):
            n = len(arr)

            for i in range(n//2 - 1, -1, -1):
                heapify(arr, n, i)

            for i in range(n-1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0)

            return arr

        return heap_sort(data)
