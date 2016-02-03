# -*- coding: utf-8 -*-

#!/usr/bin/python

import os
import sys
from datetime import datetime
import math

lib_path = os.path.abspath('../../lib')
sys.path.append(lib_path)

# controlamor el tiempo de ejecución
start_time = datetime.now()


def es_sumfactx(n):
    """ indica si un número es suma de sus factoriales """
    if n < 10:
        return False

    s = 0
    for i in str(n):
        s += math.factorial(int(i))

    return s == n

t = 0
for n in range(1, 1000000):
    if es_sumfactx(n):
        t += n

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0034:", t
