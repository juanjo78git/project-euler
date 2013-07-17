#!/usr/bin/pypy

#Project Euler 0083


import sys


def floyd_warshall(ady, nn):
    """ algoritmo de floyd-warshall para calcular el camino mínimo en un grafo
        dirigido.
        ady: matriz de adyacencias
        nd: número de nodos """
    path = ady

    for i in range(1, nn):
        path[i][i] = 0

    for k in range(0, nn):
        print('fw:', k)
        for i in range(0, nn):
            for j in range(0, nn):
                # estos valores no nos interesan, ya que de la diagonal
                # para abajo, todos los valores son infinitos.
                dt = path[i][k] + path[k][j]
                if path[i][j] > dt:
                    path[i][j] = dt

    return path


def fich_to_mat(fichero, dim):
    """ del fichero a una matriz normal """
    m = [[0 for col in range(dim)] for row in range(dim)]
    f = open(fichero, 'r')

    x = 0
    for linea in f:
        y = 0
        for i in linea.split(','):
            m[x][y] = float(i)
            y += 1
        x += 1
    f.close()

    return m


def mat_to_ady(m, dim):
    """ la matriz, la dimension de la matriz """
    nn = dim*dim
    ady = [[0 for col in range(nn)] for row in range(nn)]

    for i in range(0, nn):
        for j in range(0, nn):
            ady[i][j] = float('inf')

    for i in range(0, dim):
        for j in range(0, dim):

            ady_orig = (i*dim)+j

            # arriba
            if i > 0:
                ady_arr = ((i-1)*dim)+j
                ady[ady_orig][ady_arr] = m[i-1][j]
                if j == 0 and i == 0:
                    ady[ady_orig][ady_arr] += m[i][j]

            # derecha
            if j < dim-1:
                ady_der = (i*dim)+j+1
                ady[ady_orig][ady_der] = m[i][j+1]
                if j == 0 and i == 0:
                    ady[ady_orig][ady_der] += m[i][j]

            # izquierda
            if j > 0:
                ady_izq = (i*dim)+j-1
                ady[ady_orig][ady_izq] = m[i][j-1]
                if j == 0 and i == 0:
                    ady[ady_orig][ady_izq] += m[i][j]

            # abajo
            if i < dim-1:
                ady_abaj = ((i+1)*dim)+j
                ady[ady_orig][ady_abaj] = m[i+1][j]
                if j == 0 and i == 0:
                    ady[ady_orig][ady_abaj] += m[i][j]
    return ady


def printmat(m, dim):
    for i in range(0, dim):
        print(m[i])
    print(' ')


dim = int(sys.argv[1])
fichero = sys.argv[2]

m = fich_to_mat(fichero, dim)
#printmat(m, dim)
ady = mat_to_ady(m, dim)
#printmat(ady, dim*dim)
p = floyd_warshall(ady, dim*dim)

#printmat(p, dim*dim)


print('Resultado 0083:', p[0][(dim*dim)-1])
