#!/usr/bin/python

# It is possible to write five as a sum in exactly six different ways:
# 
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
# 
# How many different ways can one hundred be written as a sum of at least two 
# positive integers?

import os, sys
lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

import mymaths

DIF_MANERAS = 5000

def r77(lprimos, vdestino, nodo, suma, total):
    """ valor destino, nodo del que partimos, suma actual, total de aciertos """
    for i in range(nodo, vdestino):
        if suma + lprimos[i] == vdestino:
            total = total + 1
            continue
        else:
            if suma + lprimos[i] > vdestino:
                #continue
                return total
            else:
                total = r77(lprimos, vdestino, i, suma + lprimos[i], total)
    return total

# escogemos un valor suficientemente alto
lprimos = mymaths.genlprimes(DIF_MANERAS)

n = 10
while r77(lprimos, n, 0, 0, 0) < DIF_MANERAS:
    n += 1

print "Resultado 0077:", n
