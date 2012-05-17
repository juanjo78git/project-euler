#!/usr/bin/python

# PROBLEM 0054

# In the card game poker, a hand consists of five cards and are ranked, from 
# lowest to highest, in the following way:

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest
# value wins; for example, a pair of eights beats a pair of fives (see example
# 1 below). But if two ranks tie, for example, both players have a pair of
# queens, then highest cards in each hand are compared (see example 4 below); 
# if the highest cards tie then the next highest cards are compared, and so on.

# Consider the following five hands dealt to two players:

# Hand	 	Player 1	 	Player 2	 	Winner
# 1	 	5H 5C 6S 7S KD
# Pair of Fives
 	# 2C 3S 8S 8D TD
# Pair of Eights
 	# Player 2
# 2	 	5D 8C 9S JS AC
# Highest card Ace
 	# 2C 5C 7D 8S QH
# Highest card Queen
 	# Player 1
# 3	 	2D 9C AS AH AC
# Three Aces
 	# 3D 6D 7D TD QD
# Flush with Diamonds
 	# Player 2
# 4	 	4D 6S 9H QH QC
# Pair of Queens
# Highest card Nine
 	# 3D 6D 7H QD QS
# Pair of Queens
# Highest card Seven
 	# Player 1
# 5	 	2H 2D 4C 4D 4S
# Full House
# With Three Fours
 	# 3C 3D 3S 9S 9D
# Full House
# with Three Threes
 	# Player 1
# The file, poker.txt, contains one-thousand random hands dealt to two players. 
# Each line of the file contains ten cards (separated by a single space): 
# the first five are Player 1's cards and the last five are Player 2's cards. 
# You can assume that all hands are valid (no invalid characters or 
# repeated cards), each player's hand is in no specific order, and in each hand
# there is a clear winner.

# How many hands does Player 1 win?

import shlex

class Carta:
	"""Clase para guardar una carta"""
	def __init__(self, carta):
		self.color = carta[1]
		self.valor = carta[0] 

	def __str__(self):
		return "["+str(self.valor)+str(self.color)+"]"

	def cmp(self, other):
		a = self.get_numero()
		b = other.get_numero()
		return (a > b) - (a < b)
		
	def __cmp__(self, other):
		return self.cmp(other)

	def __lt__(self, other):
		return self.__cmp__(other) < 0

	def __le__(self, other):
		return self.__cmp__(other) < 0

	def __gt__(self, other):
		return self.__cmp__(other) > 0

	def __ge__(self, other):
		return self.__cmp__(other) >= 0
		
	def __eq__(self, other):
		return self.valor == other.valor

	def get_numero(self):
		if self.valor == 'T':
			return 10
		elif self.valor == 'J':
			return 11
		elif self.valor == 'Q':
			return 12
		elif self.valor == 'K':
			return 13
		elif self.valor == 'A':
			return 14
		else:
			return int(self.valor)	
		
	def get_color(self):
		return self.color
		
	def get_valor(self):
		return self.valor


class ManoDeCartas:
	"""Mano de cartas que tiene un jugador"""
	def __init__(self, lista_de_jugadas):
		self.cartas = []
		self.__dic_ocurr = {"A":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, \
						"7":0, "8":0, "9":0, "T":0, "J":0, "Q":0, "K":0}

		for jugada in lista_de_jugadas:
			carta = Carta(jugada)
			self.cartas.append(carta)
			self.__dic_ocurr[carta.get_valor()] += 1
		if len(self.cartas) != 5:
			print("Error, número de cartas distinto de 5")
		self.cartas.sort()
			
	def __str__(self):
		mano = ""
		for c in self.cartas:
			mano = mano + str(c)
		return mano
	
	def get_listacartas(self):
		listacartas = []
		for c in self.cartas:
			listacartas.append(c.get_numero())
		return listacartas
		
	def get_listavalores(self):
		listavalores = []
		for c in self.cartas:
			listavalores.append(c.get_valor())
		return listavalores	
	
	# no me termina de gustar :/
	def get_ocurr_valor(self, o):	
		""" Retorna las ocurrencias pasado un valor """
		for valor, ocurr in self.__dic_ocurr.items():
			if ocurr == o:
				return valor
		return None

	def get_dir_ocurr(self):
		return self.__dic_ocurr	
		
	def is_color(self):
		"""Indica si tiene color la mano"""
		color = self.cartas[0].get_color()
		for c in self.cartas:
			if color != c.get_color():
				return False
		return True		

	"""Escalera real"""
	def is_escalera_real(self):
		escalera_color = ['T','J','Q','K','A']
		if not self.is_color():
			return False
		else:
			if escalera_color == self.get_listavalores():
				return True
			else:
				return False
	
	""" las comparaciones """
	
	def analiza_escalera_real(self, other):
		""" 0 es son iguales... """
		if self.is_escalera_real() and not other.is_escalera_real():
			return 1
		elif not self.is_escalera_real() and other.is_escalera_real():
			return -1
		elif self.is_escalera_real() and other.is_escalera_real():
			return 0
		else:
			# con 2 indicamos que no cumple ninguno...
			return 2
			
	def analiza_poker(self, other):	
		valor1 = self.get_ocurr_valor(4)
		valor2 = other.get_ocurr_valor(4)
		
		if valor1 == None and valor2 == None:
			return 2
		elif valor1 != None and valor2 == None:
			return 1
		elif valor1 == None and valor2 != None:
			return -1
		else:
			# marcamos el color como X
			return Carta(valor1+'X').cmp(Carta(valor2+'X'))
	


class PartidaPoker:
	"""Partida de poker"""
	# le pasamos una línea del fichero...
	def __init__(self, linea_de_juego):
		lista_jugadas = shlex.split(linea_de_juego)
		self.mano_j1 = ManoDeCartas(lista_jugadas[:5])
		self.mano_j2 = ManoDeCartas(lista_jugadas[5:])
	
	def __str__(self):
		return str(self.mano_j1) + " <-VS-> " + str(self.mano_j2)
		
	def get_mano_jugador(self, jug):
		if jug == 1:
			return self.mano_j1
		else:
			return self.mano_j2
			
			
## PROBLEMA 0054 _______________________________________________________________

lmano = ['4B', '4A','4A','3A','2A']

mano1 = ManoDeCartas(lmano)


lmano = ['AA', '2A','2A','2A','AA']

mano2 = ManoDeCartas(lmano)

#print(mano1.cmp_escalera_real(mano2))

print(mano1.analiza_poker(mano2))



exit(0)



# lectura de todo el fichero...
f = open('./poker.txt')


lista_poker = f.readlines()

for poker in lista_poker:
	poker = poker.replace('\n', '')
	partida = PartidaPoker(poker)
	print(partida)





