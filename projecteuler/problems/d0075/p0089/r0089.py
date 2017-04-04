# -*- coding: utf-8 -*-

#!/usr/bin/python

from datetime import datetime


class Roman:
    """ Número romano... """
    def __init__(self, romano):
        self._romval = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                        'M': 1000}

        self._romvalinv = {v: k for k, v in self._romval.items()}

        # reglas de resta
        self._lawsub = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}

        self._values = {900: 'CM', 400: 'CD', 90: 'XC', 40: 'XL', 9: 'IX',
                        4: 'IV'}

        self._romano = romano
        self._numero = self._calc_numero()
        self._rommin = romano

    def get_number(self):
        return self._numero

    def _calc_numero(self):
        """ calculamos a partir del romano el número en arábico """
        total = 0
        prev = None
        next = None
        curr = None
        lenr = len(self._romano)
        for r in range(0, lenr):
            # calculamos curr y next...
            curr = self._romano[r]
            if r + 1 < lenr:
                next = self._romano[r + 1]
            else:
                next = None

            if r - 1 >= 0:
                prev = self._romano[r - 1]

            if (prev is None or self._romval[prev] >= self._romval[curr]):
                if (next is None or self._romval[curr] >= self._romval[next]):
                    total += self._romval[curr]
            # cuando anterior no es ni None ni mayor igual, osea el anterior
            # es MENOR
            else:
                total += self._romval[curr] - self._romval[prev]

        # Para comprobar con la librería roman de python, pero hay números que
        # no detecta bien la librería y que mi clase si lo hace.
        #try:
            #if roman.fromRoman(self._romano) != total:
                #print "No son iguales!!!", self._romano
        #except:
            #print "Error! en, ", self._romano

        return total

    def _calc_roman(self):
        """ calcula el número romano a partir del número """

        n = self._numero
        roman = []

        # primero los miles, que no es posible agruparlos
        while (n >= 1000):
            roman.append(self._romvalinv[1000])
            n -= 1000

        # intentamos centenas
        if n >= 900:
            roman.append(self._values[900])
            n -= 900

        if n > 499:
            roman.append(self._romvalinv[500])
            n -= 500

        if n > 399:
            roman.append(self._values[400])
            n -= 400

        while n >= 100:
            roman.append(self._romvalinv[100])
            n -= 100

        # intentamos las decenas
        if n >= 90:
            roman.append(self._values[90])
            n -= 90

        if n > 49:
            roman.append(self._romvalinv[50])
            n -= 50

        if n > 39:
            roman.append(self._values[40])
            n -= 40

        while n >= 10:
            roman.append(self._romvalinv[10])
            n -= 10

        # intentamos las unidades
        if n >= 9:
            roman.append(self._values[9])
            n -= 9

        if n > 4:
            roman.append(self._romvalinv[5])
            n -= 5

        if n > 3:
            roman.append(self._values[4])
            n -= 4

        while n >= 1:
            roman.append(self._romvalinv[1])
            n -= 1

        return ''.join(roman)


# controlamor el tiempo de ejecución
start_time = datetime.now()

len_org = 0
len_fin = 0

for l in open('roman.txt'):
    s = l.strip('\n')
    r = Roman(s)

    len_org += len(s)
    n = r._calc_numero()
    len_fin += len(r._calc_roman())


print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0089: ", len_org - len_fin
