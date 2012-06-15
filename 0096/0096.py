#! /usr/bin/python



class Sudoku:
	"""Un sudoku!!"""
	def __init__(self, cadena):
		self.sudoku = []
		for i in range(len(cadena)):
			self.sudoku.append(int(cadena[i]))

	#def __str__(self):
	#	return self."
	def __str__(self):
		s = ""
		for i in range(9):
			if i % 3 == 0:
				s += "+-----+-----+-----+\n"
			for j in range(9):
			 	if j % 3 == 0:
			 		s += "|"
			 	s += str(self.sudoku[(i*9)+j])
			 	if (j+1) % 3 != 0:
			 		s += " "
			 	
			 	if (j+1) % 9 == 0:
			 		s += "|"

			s += "\n"
		s += "+-----+-----+-----+"
		return s	

	""" devuelve la fila n """
	def getfila(self, n):
		return self.sudoku[(9*n):((9*n)+9)]

	""" mira que número falta en el cubo n """
	def getmissnumcube(self, n):
		miss = [1,2,3,4,5,6,7,8,9]
		
		cube = self.getcube(n)
		for i in range(9):
			if cube[i] != 0:
				miss.remove(int(cube[i]))
	
	""" le paso una columna de la 0 a la 8 y me devuelve los datos... """ 
	def getcolumn(self, n):
		column = []
		for j in range(9):
			column.append(self.sudoku[n+(j*9)])
		
		return column

	""" le paso una fila de la 0 a la 8 y me devuelve los datos... """ 
	def getcubo(self, n):
		cubo = []
		for c in range(3)
			rango = 
			cubo += self.sudoku



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


sudoku = Sudoku("023456789123456789223456789123456789123456789123456789123456789123456789123456789")

print(sudoku)


print(sudoku.getcube(2))
#print(sudoku.getcolumn(8))





