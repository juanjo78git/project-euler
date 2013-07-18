# -*- coding: utf-8 -*-

#!/usr/bin/python

import os
import sys
from datetime import datetime

lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

import mymaths


def es_capicula10_2(n):
    return (mymaths.isstringpalindrome(str(n))
            and mymaths.isstringpalindrome(bin(n)[2:]))

LIMITE = 1000000

# controlamor el tiempo de ejecución
start_time = datetime.now()

s = 0
for n in range(1, LIMITE):
    if es_capicula10_2(n):
        s += n


print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0036:", s
