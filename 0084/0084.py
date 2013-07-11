# -*- coding: utf-8 -*-

#!/usr/bin/python

import random


class Monopoly(object):
    tablero = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
               'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
               'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
               'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']

    # definición de las cartas de suerte y de comunidad
    cc = ['GO', 'JAIL', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    ch = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'NR', 'NR', 'NU', '-3', '', '',
          '', '', '', '']

    def __init__(self, dado):
        self.dado = dado
        self.casilla = 0
        self.dobles = 0
        self.visitadas = {'GO': 1}

        # barajamos las cartas...
        random.shuffle(self.cc)
        random.shuffle(self.ch)

    def mueve(self, tirada):
        """ lo saco a función ya que quiero llamarlo también como -3 """
        self.casilla = (self.casilla + tirada) % len(self.tablero)

    def salta_a(self, casilla):
        """ salta a una casilla dada """
        self.casilla = self.tablero.index(casilla)

    def realiza_tirada(self):
        tirada = self.tirada()

        # un caso especial sería la triple tirada de dobles... ya que es
        # antes de movernos
        if self.es_tripledoble():
            self.dobles = 0
            self.salta_a('JAIL')
        else:
            # en caso de no ser triple tirada si que tenemos que movernos
            self.mueve(tirada)

            # tratamiento de ch
            #
            if self.es_ch():
                self.mueve_ch()

            # tratamiento de cc
            #
            if self.es_cc():
                self.mueve_cc()

            # tratamiento de g2j
            if self.es_g2j():
                self.salta_a('JAIL')

        # solo se suma al final, cuando hemos terminado el movimiento...
        self.suma_visita()

    def mueve_cc(self):
        # obtenemos el movimiento, como queremos simular, lo que hacemos es un
        # pop y luego un index y así tenemos la lista siempre bien...
        goto = self.cc.pop()
        self.cc.insert(0, goto)

        if goto in ('GO', 'JAIL'):
            # nos vamos a donde esté la casilla definida
            #self.casilla = self.index(goto)
            self.salta_a(goto)

    def mueve_ch(self):
        # obtenemos el movimiento, como queremos simular, lo que hacemos es un
        # pop y luego un index y así tenemos la lista siempre bien...
        goto = self.ch.pop()
        self.ch.insert(0, goto)

        if goto in ('GO', 'JAIL', 'C1', 'E3', 'H2', 'R1'):
            # nos vamos a donde esté la casilla del 'GO'
            #self.casilla = self.index(goto)
            self.salta_a(goto)
        elif goto == 'NR':
            self.mueve(self.dame_proximo_nr())
        elif goto == 'NU':
            self.mueve(self.dame_proximo_nu())
        elif goto == '-3':
            self.mueve(-3)

    def dame_proximo_nr(self):
        """ nos devuelve la próxima estación ferroviaria """
        for i in range(1, len(self.tablero) + 1):
            casilla = (i + self.casilla) % len(self.tablero)
            if self.tablero[casilla][0] == 'R':
                return casilla

    def dame_proximo_nu(self):
        """ nos devuelve la proxima compañía eléctrica """
        actual = self.get_casilla()
        for i in range(1, len(self.tablero) + 1):
            casilla = (i + self.casilla) % len(self.tablero)
            if self.tablero[casilla][0] == 'U':
                return casilla

    def suma_visita(self):
        """ sumamos a nuestro diccionario una nueva visita """
        casilla = self.get_casilla()
        if casilla in self.visitadas:
            self.visitadas[casilla] += 1
        else:
            self.visitadas[casilla] = 1

    def get_casilla(self):
        """ retorna el valor de la casilla donde estamos, por ejemplo 'GO' """
        return self.tablero[self.casilla]

    def es_tripledoble(self):
        """ para el caso de triple doble """
        if self.dobles == 3:
            return True
        else:
            return False

    def es_ch(self):
        """ nos indica si la casilla actual es ch """
        casilla = self.get_casilla()
        if casilla[0:2] == 'CH':
            return True
        else:
            return False

    def es_cc(self):
        """ nos indica si la casilla actual es cc """
        casilla = self.get_casilla()
        if casilla[0:2] == 'CC':
            return True
        else:
            return False

    def es_g2j(self):
        """ nos indica si la casilla actual es g2j """
        casilla = self.get_casilla()
        if casilla == 'G2J':
            return True
        else:
            return False

    def tirada(self):
        """ nos devuelve el valor de la tirada """
        d1 = random.randint(1, self.dado)
        d2 = random.randint(1, self.dado)

        if d1 == d2:
            self.dobles += 1
        else:
            self.dobles = 0

        return d1 + d2

m = Monopoly(6)
for i in range(1, 1000000000):
    m.realiza_tirada()

l = []
for i in m.visitadas:
    l.append([m.visitadas[i], i])

for i in sorted(l):
    print i, m.tablero.index(i[1])
