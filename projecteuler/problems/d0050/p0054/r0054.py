# -*- coding: utf-8 -*-

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

# If two players have the same ranked hands then the rank made up of the
# highest value wins; for example, a pair of eights beats a pair of fives (see
# example
# 1 below). But if two ranks tie, for example, both players have a pair of
#   queens, then highest cards in each hand are compared (see example 4 below);
#   if the highest cards tie then the next highest cards are compared, and so
#   on.

# Consider the following five hands dealt to two players:

# Hand         Player 1         Player 2         Winner
# 1         5H 5C 6S 7S KD
# Pair of Fives
     # 2C 3S 8S 8D TD
# Pair of Eights
     # Player 2
# 2         5D 8C 9S JS AC
# Highest card Ace
     # 2C 5C 7D 8S QH
# Highest card Queen
     # Player 1
# 3         2D 9C AS AH AC
# Three Aces
     # 3D 6D 7D TD QD
# Flush with Diamonds
     # Player 2
# 4         4D 6S 9H QH QC
# Pair of Queens
# Highest card Nine
     # 3D 6D 7H QD QS
# Pair of Queens
# Highest card Seven
     # Player 1
# 5         2H 2D 4C 4D 4S
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
        self.__dic_ocurr = {"A": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
                            "6": 0, "7": 0, "8": 0, "9": 0, "T": 0, "J": 0,
                            "Q": 0, "K": 0}

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
    def repetidas_valor(self, o):
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

    def is_escalera_real(self):
        """Escalera real"""
        escalera_color = ['T', 'J', 'Q', 'K', 'A']
        return escalera_color == self.get_listavalores() and self.is_color()

    def is_escalera(self):
        for i in range(0, 4):
            num1 = self.cartas[i].get_numero()
            num2 = self.cartas[i+1].get_numero()
            if num1 + 1 != num2:
                return False
        return True

    def is_escalera_color(self):
        return (self.is_escalera() and self.is_color()
                and not self.is_escalera_real())

    def is_poker_of(self):
        return self.repetidas_valor(4)

    def is_full_of(self):
        valor3 = self.repetidas_valor(3)
        valor2 = self.repetidas_valor(2)

        if valor3 and valor2:
            return valor3, valor2
        else:
            return None, None

    def is_trio_of(self):
        valor3 = self.repetidas_valor(3)
        valor2 = self.repetidas_valor(2)

        if valor3 and not valor2:
            return valor3
        else:
            return None

    def is_two_pair_of(self):
        pares = []
        for valor, ocurr in self.__dic_ocurr.items():
            if ocurr == 2:
                pares.append(valor)
        if len(pares) == 2:
            pares.sort()
            return pares[0], pares[1]
        else:
            return None, None

    def is_one_pair_of(self):
        return self.repetidas_valor(2)

    # las comparaciones

    # 1. escalera real!
    def analiza_escalera_real(self, other):
        """ 0 es son iguales... """
        escal1 = self.is_escalera_real()
        escal2 = other.is_escalera_real()

        if escal1 and not escal2:
            return 1
        elif not escal1 and escal2:
            return -1
        elif escal1 and escal2:
            return 0
        else:
            # con 2 indicamos que no cumple ninguno...
            return 2

    # 2. escalera color
    def analiza_escalera_color(self, other):
        escal1 = self.is_escalera_color()
        escal2 = other.is_escalera_color()

        if escal1 and not escal2:
            return 1
        elif not escal1 and escal2:
            return -1
        elif escal1 and escal2:
            return self.cartas[4].cmp(other.cartas[4])
        else:
            # con 2 indicamos que no cumple ninguno...
            return 2

    # 3. poker
    def analiza_poker(self, other):
        valor1 = self.is_poker_of()
        valor2 = other.is_poker_of()

        if not valor1 and not valor2:
            return 2
        elif valor1 and not valor2:
            return 1
        elif not valor1 and valor2:
            return -1
        else:
            # marcamos el color como X
            return Carta(valor1+'X').cmp(Carta(valor2+'X'))

    # 4. full
    def analiza_full(self, other):
        val3s, val2s = self.is_full_of()
        val3o, val2o = other.is_full_of()

        if val3s and not val3o:
            return 1
        elif not val3s and val3o:
            return -1
        elif val3s and val3o:
            # no puede haber dos trios iguales
            return Carta(val3s+'X').cmp(Carta(val3o+'X'))
        else:
            return 2

    # 5. color
    def analiza_color(self, other):
        col1 = self.is_color()
        col2 = other.is_color()

        if col1 and not col2:
            return 1
        elif not col1 and col2:
            return -1
        elif col1 and col2:
            return self.analiza_mayor(other)
        else:
            # con 2 indicamos que no cumple ninguno...
            return 2

    # 6. escalera
    def analiza_escalera(self, other):
        escal1 = self.is_escalera()
        escal2 = other.is_escalera()

        if escal1 and not escal2:
            return 1
        elif not escal1 and escal2:
            return -1
        elif escal1 and escal2:
            return self.analiza_mayor(other)
        else:
            # con 2 indicamos que no cumple ninguno...
            return 2

    # 7. trio
    def analiza_trio(self, other):
        val3s = self.is_trio_of()
        val3o = other.is_trio_of()

        if val3s and not val3o:
            return 1
        elif not val3s and val3o:
            return -1
        elif val3s and val3o:
            return Carta(val3s+'X').cmp(Carta(val3o+'X'))
        else:
            return 2

    # 8. dobles parejas
    def analiza_doble_pareja(self, other):
        # el par 2 será mayor, ya que viene en orden
        par1s, par2s = self.is_two_pair_of()
        par1o, par2o = other.is_two_pair_of()
        if par1s and par1o:
            comp = Carta(par2s+'X').cmp(Carta(par2o+'X'))
            if comp == 0:
                return Carta(par1s+'X').cmp(Carta(par1o+'X'))
            else:
                return comp
        elif par1s and not par1o:
            return 1
        elif not par1s and par1o:
            return -1
        else:
            return 2

    # 9. pareja
    def analiza_pareja(self, other):
        pars = self.is_one_pair_of()
        paro = other.is_one_pair_of()

        if pars and paro:
            return Carta(pars+'X').cmp(Carta(paro+'X'))
        elif pars and not paro:
            return 1
        elif not pars and paro:
            return -1
        else:
            return 2

    # 10. carta mayor
    def analiza_mayor(self, other):
        return self.cartas[4].cmp(other.cartas[4])

    def __cmp__(self, other):

        # 1. escalera real
        comp = self.analiza_escalera_real(other)
        if comp != 2:
            return comp

        # 2. escalera color
        comp = self.analiza_escalera_color(other)
        if comp != 2:
            return comp

        # 3. poker
        comp = self.analiza_poker(other)
        if comp != 2:
            return comp

        # 4. full
        comp = self.analiza_full(other)
        if comp != 2:
            return comp

        # 5. color
        comp = self.analiza_color(other)
        if comp != 2:
            return comp

        # 6. escalera
        comp = self.analiza_escalera(other)
        if comp != 2:
            return comp

        # 7. trio
        comp = self.analiza_trio(other)
        if comp != 2:
            return comp

        # 8. dobles parejas
        comp = self.analiza_doble_pareja(other)
        if comp != 2:
            return comp

        # 9. pareja
        comp = self.analiza_pareja(other)
        if comp != 2:
            return comp

        # 10. carta mayor
        return self.analiza_mayor(other)

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


## PROBLEMA 0054 ______________________________________________________________

# lectura de todo el fichero...
f = open('./poker.txt')

total = 0
lista_poker = f.readlines()

for poker in lista_poker:
    poker = poker.replace('\n', '')
    partida = PartidaPoker(poker)

    if partida.get_mano_jugador(1) > partida.get_mano_jugador(2):
        total += 1

print("Total partidas ganas por player1: ", total)
