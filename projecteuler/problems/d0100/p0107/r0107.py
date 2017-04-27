# https://github.com/israelst/Algorithms-Book--Python/blob/master/
#       5-Greedy-algorithms/kruskal.py
# Vaya vaya, vaya un robo, pero limpio el algoritmo que vaya una guarra de
# variables globales...

import os


def kruskal(graph):

    def _make_set(parent, rank, vertice):
        parent[vertice] = vertice
        rank[vertice] = 0

    def _find(parent, vertice):
        if parent[vertice] != vertice:
            parent[vertice] = _find(parent, parent[vertice])
        return parent[vertice]

    def _union(parent, rank, vertice1, vertice2):
        root1 = _find(parent, vertice1)
        root2 = _find(parent, vertice2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]: rank[root2] += 1

    parent = dict()
    rank = dict()

    for vertice in graph['vertices']:
        _make_set(parent, rank, vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if _find(parent, vertice1) != _find(parent, vertice2):
            _union(parent, rank, vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree

# graph = {
#         'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
#         'edges': set([
#             (1, 'A', 'B'),
#             (5, 'A', 'C'),
#             (3, 'A', 'D'),
#             (4, 'B', 'C'),
#             (2, 'B', 'D'),
#             (1, 'C', 'D'),
#             ])
#         }
# minimum_spanning_tree = set([
#             (1, 'A', 'B'),
#             (2, 'B', 'D'),
#             (1, 'C', 'D'),
#             ])
# print(kruskal(graph))
# assert kruskal(graph) == minimum_spanning_tree

# graph = {
#         'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
#         'edges': set([
#             (16, 'A', 'B'),
#             (12, 'A', 'C'),
#             (21, 'A', 'D'),
#             (17, 'B', 'D'),
#             (20, 'B', 'E'),
#             (28, 'C', 'D'),
#             (31, 'C', 'F'),
#             (18, 'D', 'E'),
#             (19, 'D', 'F'),
#             (23, 'D', 'G'),
#             (11, 'E', 'G'),
#             (27, 'F', 'G'),
#             ])
#         }
# print(kruskal(graph))
def result():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    fichero = os.path.join(ROOT_DIR, 'p107_network_example.txt')

    f = open(fichero, 'r') 

    m = []
    for line in f:
        # print(line.replace('\n', ''))
        a = line.replace('\n', '').split(',')
        # print(a)
        m.append(a)
    print(m)
