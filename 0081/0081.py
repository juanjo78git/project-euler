#!/usr/bin/pypy

#Project Euler 0081

#In the 5 by 5 matrix below, the minimal path sum from the top left to the 
#bottom right, by only moving to the right and down, is indicated in bold red 
#and is equal to 2427.


#131	673	234	103	18
#201	96	342	965	150
#630	803	746	422	111
#537	699	497	121	956
#805	732	524	37	331

#Find the minimal path sum, in matrix.txt (right click and 'Save Link/
#Target As...'), a 31K text file containing a 80 by 80 matrix, from the top 
#left to the bottom right by only moving right and down.

import sys

# algoritmo de floyd-warshall para calcular el camino mínimo en un grafo
# dirigido.
# ady: matriz de adyacencias
# nd: número de nodos
def floyd_warshall(ady, nn):
	path = ady
	orig = path[0][0]
	
	for i in range(1, nn):
		path[i][i] = 0

	for k in range(0, nn):
		#print('fw:', k)
		for i in range(0, nn):
			for j in range(0, nn):
				# estos valores no nos interesan, ya que de la diagonal 
				# para abajo, todos los valores son infinitos.
				if i > j:
					break
				dt = path[i][k] + path[k][j]
				if path[i][j] > dt:
					path[i][j] = dt
	
	return path

# del fichero a una matriz normal
def fich_to_mat(fichero, dim):
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
	
# la matriz, la dimension de la matriz	
def mat_to_ady(m, dim):	
	nn = dim*dim
	ady = [[0 for col in range(nn)] for row in range(nn)]
	
	for i in range(0, nn):
		for j in range(0, nn):
			ady[i][j] = float('inf')
	
	for i in range(0, dim):
		for j in range(0, dim):
			
			ady_orig = (i*dim)+j

			# derecha
			if j < dim-1:
				ady_der = (i*dim)+j+1
				ady[ady_orig][ady_der] = m[i][j+1]
				# añado, que al salir desde el inicio, ya sumamos...
				if j == 0:
					ady[ady_orig][ady_der] += m[i][j]					

			# abajo	
			if i < dim-1:
				ady_abaj = ((i+1)*dim)+j
				ady[ady_orig][ady_abaj] = m[i+1][j]			
				if j == 0:
					ady[ady_orig][ady_abaj] += m[i][j]	

	
	return ady


def printmat(m, dim):
	for i in range(0, dim):
		print(m[i])
	print(' ')
	

dim = int(sys.argv[1])
fichero = sys.argv[2]

m = fich_to_mat(fichero, dim)
ady = mat_to_ady(m, dim)
p = floyd_warshall(ady, dim*dim)

print('Resultado 0081:', int(p[0][(dim*dim)-1]))

