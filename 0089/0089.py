# -*- coding: utf-8 -*-

#!/usr/bin/pypy


class Romans:
    """ Número romano... """
    def __init__(self, romano):
        self._romval = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                        'M': 1000}

        # reglas de resta
        self._lawsub = {'I': ['V', 'C'], 'X': ['L', 'C'], 'C': ['D', 'M']}

        self._romano = romano
        self._numero = 0

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

        return total


#r1 = Romans('CXIV')
r1 = Romans('MMMMDCLXXII')

print r1._calc_numero()











# controlamos el tiempo de ejecución
#start_time = datetime.now()


#print "Tiempo total: ", datetime.now() - start_time
#print "Resultado de 0179: ", total
