# -*- coding: utf-8 -*-

#!/usr/bin/python

import os
import sys
from datetime import datetime

lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

# controlamor el tiempo de ejecución
start_time = datetime.now()


def es_sumpotx(n, p):
    """ indica si un número es suma de su pontencia p, importante: SUMA, es
        necesario que el número sea por tanto mayor que 9 """
    if n < 10:
        return False

    s = 0
    for i in str(n):
        s += int(i) ** p

    return s == n

t = 0
for n in range(1, 1000000):
    if es_sumpotx(n, 5):
        t += n

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0030:", t
