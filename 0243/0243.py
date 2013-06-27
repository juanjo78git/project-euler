# -*- coding: utf-8 -*-

#!/usr/bin/python

# A positive fraction whose numerator is less than its denominator is called
# a proper fraction.
#
# For any denominator, d, there will be d1 proper fractions; for example,
# with d = 12
# 1/12, 2/12, 3/12, 4/12, 5/12, 6/12, 7/12, 8/12, 9/12, 10/12, 11/12.
#
# We shall call a fraction that cannot be cancelled down a resilient fraction.
# Furthermore we shall define the resilience of a denominator, R(d), to be
# the ratio of its proper fractions that are resilient; for example,
# R(12) = 4/11 .
# In fact, d=12 is the smallest denominator having a resilience R(d) < 4/10 .
#
# Find the smallest denominator d, having a resilience R(d) < 15499/94744 .

import os
import sys
lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

import mymaths

from datetime import datetime


def R_mayor(n, d, min_n, min_d):
    """ está claro que si llegamos a un punto donde ya es mayor, mejor nos
        olvidamos, no vamos a poder sacar ese número """
    return (min_d * n) >= ((d - 1) * min_n)


#LIMITE = 10000000

# controlamor el tiempo de ejecución
start_time = datetime.now()

min_d = 94744
min_n = 15499
d = 1700000

#lp = mymaths.genlprimes(LIMITE)

#print "Generación de lista de primos terminada"

while True:
    d += 1

    if d % 1000 == 0:
        print d

    noreducibles = mymaths.euler_phi(d)

    # vemos si es posible que sea solucion
    if not R_mayor(noreducibles, d, min_n, min_d):
        break


# si salimos es que tenemos solucion...
print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 243: ", d
