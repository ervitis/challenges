# -*- coding: utf-8 -*-

from collections import defaultdict


class Graph(object):

    def __init__(self):
        self._graph = defaultdict(list)
        self._path = []

    def add_edge_union(self, u, v):
        self._graph[u].append(v)
        return self

    def dfs(self, node):
        if node not in self._path:
            self._path.append(node)
            for n in self._graph[node]:
                self.dfs(n)

    def __repr__(self):
        return ' '.join(self._path)


if __name__ == '__main__':
    g = Graph()\
        .add_edge_union('A', 'B')\
        .add_edge_union('A', 'C')\
        .add_edge_union('B', 'D')\
        .add_edge_union('D', 'F')\
        .add_edge_union('E', 'I')\
        .add_edge_union('F', 'H')\
        .add_edge_union('H', 'I')

    g.dfs('A')

    print(g)
