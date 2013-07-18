# -*- coding: utf-8 -*-

#!/usr/bin/python

from datetime import datetime


LIMITE = 100


def sumdigits(n):
    return sum([int(i) for i in str(n)])


# controlamor el tiempo de ejecución
start_time = datetime.now()

m = 0
for a in range(1, LIMITE + 1):
    for b in range(1, LIMITE + 1):
        m = max(m, sumdigits(a ** b))

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0056:", m
