# -*- coding: utf-8 -*-

class Graph:
    def __init__(self):
        self.graph = { 'vertices': [],
                       'edges': set([]) }


    def add_edge(self, edge):
        edges = list(self.graph['edges'])
        vertices = list(self.graph['vertices'])

        if edge[1] not in self.graph['vertices']:
            self.graph['vertices'].append(edge[1])
        
        if edge[2] not in self.graph['vertices']:
            self.graph['vertices'].append(edge[2])
        
        self.graph['edges'].add(edge)

    def weight(self):
        t = 0
        for edge in self.graph['edges']:
            t += edge[0]
        return t

    def from_file_adjacency_matrix(self, filepath):
        f = open(filepath, 'r') 

        m = []
        for line in f:
            a = line.replace('\n', '').split(',')
            m.append(a)
    
        for i in range(0, len(m[0])):
            for j in range(i + 1, len(m[0])):
                if m[i][j] != '-':
                    vi = 'V{}'.format(i)
                    vj = 'V{}'.format(j)
                    vw = int(m[i][j])
                    self.add_edge((vw, vi, vj))

    def kruskal(self):
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

        for vertice in self.graph['vertices']:
            _make_set(parent, rank, vertice)

        minimum_spanning_tree = set()
        edges = list(self.graph['edges'])
        edges.sort()
        for edge in edges:
            weight, vertice1, vertice2 = edge
            if _find(parent, vertice1) != _find(parent, vertice2):
                _union(parent, rank, vertice1, vertice2)
                minimum_spanning_tree.add(edge)
        # return minimum_spanning_tree
        self.graph['edges'] = minimum_spanning_tree


