# -*- coding: utf-8 -*-

#!/usr/bin/python

from datetime import datetime


def get_camino_minimo(a, b, c):
    return (a**2 + ((b + c)**2))**0.5


def tiene_camino_entero(a, b, c):

    l1 = get_camino_minimo(a, b, c)
    l2 = get_camino_minimo(c, a, b)
    l3 = get_camino_minimo(b, a, c)

    cm = min(min(l1, l2), l3)

    return cm == int(cm)

# controlamor el tiempo de ejecución
start_time = datetime.now()

# no
M = 1815
count = 0
LIMITE = 1000000

while count < LIMITE:
    print M, count
    count = 0
    M += 1
    for a in range(1, M + 1):
        for b in range(a, M + 1):
            for c in range(b, M + 1):
                if tiene_camino_entero(a, b, c):
                    count += 1

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0085: ", count, M
