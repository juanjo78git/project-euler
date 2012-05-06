#! /usr/bin/python2


# vamos a ver como lo puedo montar

# le pasamos una matriz 3x3 y nos devuelve una lista con los numeros que del
# 1 al 9 faltan
def get_list_num_faltan_m3(matriz):
	
	faltan = [1,2,3,4,5,6,7,8,9]

	#for i in range(3):
	#	for j in range(3):
	#		if m3[i][j] != 0:
	#			faltan.remove(m3[i][j])


	for fila in matriz:
		for i in fila:
			if i != 0:
				faltan.remove(i)

	return faltan
	

# notas: con el mod, podemos quedarnos con con el minicuadrado de 3x3:
#


a = ([[1,2,3], [4,5,0], [0,7,8]])


f = get_list_num_faltan_m3(a)

print f


z = [[0,0,3,0,2,0,6,0,0],
[9,0,0,3,0,5,0,0,1],
[0,0,1,8,0,6,4,0,0],
[0,0,8,1,0,2,9,0,0],
[7,0,0,0,0,0,0,0,8],
[0,0,6,7,0,8,2,0,0],
[0,0,2,6,0,9,5,0,0],
[8,0,0,2,0,3,0,0,9]]


z1 = [[0,0,3,0,2,0,6,0,0],
[9,0,0,3,0,5,0,0,1],
[0,0,1,8,0,6,4,0,0],
[0,0,8,1,0,2,9,0,0],
[7,0,0,0,0,0,0,0,8],
[0,0,6,7,0,8,2,0,0],
[0,0,2,6,0,9,5,0,0],
[8,0,0,2,0,3,0,0,9]]

print z

print z[1][3]

print z[3][1]













