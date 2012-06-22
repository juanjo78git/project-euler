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

	
	def getfila(self, n):
		""" devuelve la fila n """
		return self.sudoku[(9*n):((9*n)+9)]


	def getmissnumcube(self, n):
		""" mira que numero falta en el cubo n """
		miss = [1,2,3,4,5,6,7,8,9]
		
		cube = self.getcube(n)
		for i in range(9):
			if cube[i] != 0:
				miss.remove(int(cube[i]))
	
	
	def getcolumn(self, n):
		""" le paso una columna de la 0 a la 8 y me devuelve los datos... """ 
		column = []
		for j in range(9):
			column.append(self.sudoku[n+(j*9)])
		
		return column

	def getcube(self, n):
		""" le paso una fila de la 0 a la 8 y me devuelve los datos... """ 
		cubo = []
		for f in range(3):
			for i in range(3):
				e = (27 * (n / 3)) + (f * 9) + i + ((n % 3) * 3)
				cubo.append(self.sudoku[e])
		return cubo

	def is_valid_partial(self, partial):
		""" si una linea, cubo y columna es valida """
		complet = [1,2,3,4,5,6,7,8,9]
		for i in partial:
			if i != 0:
				if i not in complet:
					return False
				else:
					complet.remove(i)
		return True
		
	def is_valid(self):
		""" si es valido, no si es solucion """
		for i in range(9):
			if not self.is_valid_partial(self.getcube(i)):
				return False
			if not self.is_valid_partial(self.getcolumn(i)):
				return False
			if not self.is_valid_partial(self.getfila(i)):
				return False
		return True
				

	def is_solved_partial(self, partial):
		if [1,2,3,4,5,6,7,8,9] == partial.sort():
			return True
		else:
			False
		
	def is_solved(self):
		""" si es solucion """
		for i in range(9):
			if not self.is_solved_partial(self.getcube(i)):
				return False
			if not self.is_solved_partial(self.getcolumn(i)):
				return False
			if not self.is_solved_partial(self.getfila(i)):
				return False
		return True
		
		
				
# vamos a ver como lo puedo montar

# notas: con el mod, podemos quedarnos con con el minicuadrado de 3x3:
#


a = ([[1,2,3], [4,5,0], [0,7,8]])





#sudoku = Sudoku("023456789123456789223456789123456789123456789123456789123456789123456789777888999")

sudoku = Sudoku("300200000000107000706030500070009080900020004010800050009040301000702000000008006")

print(sudoku)


print(sudoku.getcube(0))
print(sudoku.getcube(1))
print(sudoku.getcube(2))
print(sudoku.getcube(3))
print(sudoku.getcube(8))
print(sudoku.is_valid())
print(sudoku.is_solved())
#print(sudoku.getcolumn(8))





