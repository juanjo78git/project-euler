#! /usr/bin/python



class Sudoku:
	"""Un sudoku!!"""
	def __init__(self, cadena):
		self.__sudoku = []
		for i in range(len(cadena)):
			self.__sudoku.append(int(cadena[i]))

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
			 	s += str(self.__sudoku[(i*9)+j])
			 	if (j+1) % 3 != 0:
			 		s += " "
			 	
			 	if (j+1) % 9 == 0:
			 		s += "|"

			s += "\n"
		s += "+-----+-----+-----+"
		return s	

	# @TODO: porfavor, hay que limpiar este metodo
	def getpossibles(self, i):
		""" devuelve la lista de posibles! """
		if self.__sudoku[i] != 0:
			return []

		c, i, j = self.getcord(i) 
		cubo = self.getcube(c)
		fila = self.getfile(i)
		columna = self.getcolumn(j)

		miss = self.getmissnumcube(c)
		poss = list(miss)

		for m in miss:
			if m in fila or m in columna:
				poss.remove(m)
		return poss
		

	def getcord(self, i):
		""" retorna las cordenadas """
		# @TODO repasar, que python3 no me gusta mucho lo de dividir :(
		cubo = ((i//27)*3 + (i//3)%3)
		fila, columna = divmod(i, 9)
		return cubo, fila, columna
		
	
	def getfile(self, n):
		""" devuelve la fila n """
		return self.__sudoku[(9*n):((9*n)+9)]


	def getmissnumcube(self, n):
		""" mira que numero falta en el cubo n """
		miss = [1,2,3,4,5,6,7,8,9]
		
		cube = self.getcube(n)
		for i in range(9):
			if cube[i] != 0:
				miss.remove(int(cube[i]))
		return miss
	
	
	def getcolumn(self, n):
		""" le paso una columna de la 0 a la 8 y me devuelve los datos... """ 
		column = []
		for j in range(9):
			column.append(self.__sudoku[n+(j*9)])
		
		return column

	def getcube(self, n):
		""" le paso uno de los cubos y devuelve los datos que tiene... """ 
		cubo = []
		for f in range(3):
			for i in range(3):
				e = (27 * (n / 3)) + (f * 9) + i + ((n % 3) * 3)
				cubo.append(self.__sudoku[e])
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
			if not self.is_valid_partial(self.getfile(i)):
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
			if not self.is_solved_partial(self.getfile(i)):
				return False
		return True

	# seria recursivo, pero no lo tengo claro..., dejo un esbozo.	
	def resolve(self):
		if self.is_solved():
			self.__str__()
			return True
		else:
			ind = -1
			for i in range(81):
				if self.__sudoku[i] == 0:
					ind = i
					break
			
			poss = self.getpossibles(ind)
			print(poss, '#', ind)
			print(self)
			for p in poss:
				self.__sudoku[ind] = p
				self.__str__()
				if self.is_valid():
					salida = self.resolve()
				else:
					self.__sudoku[ind] = 0
		
				
# vamos a ver como lo puedo montar

# notas: con el mod, podemos quedarnos con con el minicuadrado de 3x3:
#

#sudoku = Sudoku("023456789123456789223456789123456789123456789123456789123456789123456789777888999")

sudoku = Sudoku("300200000000107000706030500070009080900020004010800050009040301000702000000008006")

print(sudoku)


#print(sudoku.getcube(0))
#print(sudoku.getcube(1))
#print(sudoku.getcube(2))
#print(sudoku.getcube(3))
#print(sudoku.getcube(8))
#print(sudoku.is_valid())
#print(sudoku.is_solved())
#print(sudoku.getcord(80))
#print(sudoku.getcord(22))
#print(sudoku.getpossibles(1))
sudoku.resolve()
#print(sudoku.getcolumn(8))





