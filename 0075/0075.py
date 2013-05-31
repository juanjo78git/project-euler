# -*- coding: utf-8 -*-

#!/usr/bin/pypy

import os
import sys
from datetime import datetime

lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

import mymaths
import math


LIMITE = 1000000

# controlamos el tiempo de ejecución
start_time = datetime.now()

for a in range(1, LIMITE):
    for b in range(1, LIMITE):
        c = math.sqrt((a**2) + (b**2))
        if c == int(c):
            print a, b, c

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0075: "
