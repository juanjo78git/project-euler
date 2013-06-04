# -*- coding: utf-8 -*-

#!/usr/bin/pypy

import os
import sys
from datetime import datetime

lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

import mymaths

MAXIMO = 10000000000


def get_resto(n, p):
    return (((p - 1) ** n) + (p + 1) ** n) % (p ** 2)


# controlamos el tiempo de ejecución
start_time = datetime.now()

# generador de primos
primegen = mymaths.prime()

n = 0
while True:
    p = primegen.next()
    n += 1
    r = get_resto(n, p)
    if r > MAXIMO:
        break

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0123 ", n
