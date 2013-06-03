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
        suma = 0
        resta = 0
        total = 0
        ant = None
        for i in self._romano:
            if ant is None:
                suma += self._romval[i]
            else:
                # vemos si es de tipo resta...
                if i in self._lawsub:
                    resta += self._romval[i]

        # nos quedaban unos valores que parecían resta pero no lo son...
        if resta > 0:
            suma += resta

        total = suma
        return total


r = Romans('XI')

print r._calc_numero()











# controlamos el tiempo de ejecución
#start_time = datetime.now()


#print "Tiempo total: ", datetime.now() - start_time
#print "Resultado de 0179: ", total
