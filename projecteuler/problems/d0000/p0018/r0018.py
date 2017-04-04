# -*- coding: utf-8 -*-


# dos argumentos, la dimensión y el fichero txt

# import sys
import os


class Graph:
    """ un grafo """
    def __init__(self, g):
        self.g = g

    def V(self):
        return self.g.keys()

    def Adj(self, v):
        return self.g[v].keys()

    def w(self, u, v):
        return self.g[u][v]


def obten_matriz_fichero(dimension, fichero):
    """ a partir de un fichero y con la dimension dada, obtiene una matriz con
        los datos leidos """

    # creamos la matriz para guardar los datos
    m = [[0 for col in range(dimension)] for row in range(dimension)]
    x = 0
    f = open(fichero, 'r')

    for linea in f:
        y = 0
        for i in linea.split(' '):
            m[x][y] = int(i)
            y = y + 1
        x = x + 1
    f.close()
    return m


def matriz_a_grafo(dimension, matriz):
    """ pasamos la matriz a un grafo, muy bonito """

    # lo tengo casi!
    dic = {}

    for i in range(dimension-1):
        for j in range(dimension-1):
            if j <= i:
                origen = str(i) + '-' + str(j)
                dest1 = str(i + 1) + '-' + str(j)
                dest2 = str(i + 1) + '-' + str(j + 1)

                dic[origen] = {dest1: -matriz[i + 1][j],
                               dest2: -matriz[i + 1][j+1]}

    # el primer nodo
    dic['x-x'] = {'0-0': -matriz[0][0]}

    for i in range(dimension):
        origen = str(dimension - 1) + '-' + str(i)
        dic[origen] = {}

    #return Graph(dic)
    return dic


# bajada de internet, luego lo analizamos
def initialize(graph, source):
    d = {}
    p = {}
    for node in graph:
        d[node] = float('Inf')
        p[node] = None
    d[source] = 0
    return d, p


def relax(u, v, graph, d, p):
    if d[v] > d[u] + graph[u][v]:
        d[v] = d[u] + graph[u][v]
        p[v] = u


def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, d, p)
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]
    return d, p


def result():
    # dim = int(sys.argv[1])
    # fich = sys.argv[2]
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    fich = os.path.join(ROOT_DIR, 'grafo2.txt')
    dim = 15

    mat = obten_matriz_fichero(dim, fich)


    grafo = matriz_a_grafo(dim, mat)

    p, d = bellman_ford(grafo, 'x-x')

    minimo = 0
    for i in p:
        if minimo > p[i]:
            minimo = p[i]
    
    return abs(minimo)
