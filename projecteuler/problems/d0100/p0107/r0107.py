# -*- coding: utf-8 -*-

import os

from projecteuler.classes import graph


def result():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    fichero = os.path.join(ROOT_DIR, 'p107_network.txt')

    g = graph.Graph()

    g.from_file_adjacency_matrix(fichero)

    original_weight = g.weight()

    g.kruskal()

    minimal_weight = g.weight()

    return original_weight - minimal_weight
