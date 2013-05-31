# -*- coding: utf-8 -*-

#!/usr/bin/pypy

import os
import sys
from datetime import datetime

lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

import mymaths


LIMIT = 100000000


def genlistprimeslimit(LIMIT):
    l = []
    genp = mymaths.prime()
    while True:
        p = genp.next()
        if p < ((LIMIT / 2) + 1):
            l.append(p)
        else:
            break
    return l

# controlamos el tiempo de ejecución
start_time = datetime.now()

primes = genlistprimeslimit(LIMIT)
print "Lista de primos generada, con %d elementos" % len(primes)
composites = []

for i in range(0, len(primes)):
        for j in range(i, len(primes)):
            c = primes[i] * primes[j]
            if c < LIMIT:
                composites.append(primes[i] * primes[j])
            else:
                break

#print primes
#print composites
#print len(composites)

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0187: ", len(composites)
