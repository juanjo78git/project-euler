# -*- coding: utf-8 -*-

#!/usr/bin/python

import os
import sys
from datetime import datetime

lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

diasmes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def esbisiesto(y):
    return (y % 4 == 0 and not y % 100 == 0) or (y % 400 == 0)


# controlamor el tiempo de ejecución
start_time = datetime.now()

# desplazamiento, ya que el 1 de 1901 es martes
dias = 2
total = 0
for y in range(1901, 2001):
    c = 1
    for dm in diasmes:
        while dias >= 7:
            dias = dias - 7

        if dias == 0:
            total += 1

        if dm == 28:
            if esbisiesto(y):
                dm += 1

        dias = dm + dias
        c += 1

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0019: ", total
