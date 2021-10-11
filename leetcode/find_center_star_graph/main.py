# -*- coding: utf-8 -*-

"""
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
"""
from collections import Counter
from typing import List


def find_center(edges: List[List[int]]) -> int:
    if len(edges) < 1:
        return 0

    return edges[0][edges[0][1] in edges[1]]


def main():
    print(find_center([[1, 2], [2, 3], [4, 2]]))
    print(find_center([[1, 2], [5, 1], [1, 3], [1, 4]]))


if __name__ == '__main__':
    main()
