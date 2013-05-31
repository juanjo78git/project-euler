# -*- coding: utf-8 -*-

#!/usr/bin/pypy

import os
import sys
from datetime import datetime

lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

import mymaths

# 10^7
LIMIT = 10000000


# controlamos el tiempo de ejecución
start_time = datetime.now()
nd_ant = 0
total = 0
for n in range(2, LIMIT):
    nd = mymaths.numdivs(n)
    if n % 1000 == 0:
        print n
    if nd == nd_ant:
        total += 1
    nd_ant = nd

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0179: ", total
