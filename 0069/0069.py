#!/usr/bin/python

import os, sys
lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

import mymaths

LIMIT = 1000000

def genlprimes(n):
    """ genera una lista de primos que pueda dividir n """
    l = []
    p = mymaths.prime()
    prime = p.next()
    # quiero una lista de primos que dividan a n, por lo tanto con
    # buscar solo la mitad me va bien
    limit = (n * 0.5) + 1
    print limit
    while prime < limit:
        l.append(prime)
        prime = p.next() 

    return l

def numdivsprimes(lprimes, n):
    """ lista de primos que son divisibles por el numero """
    ldiv = []
    np = 0
    d = lprimes[np]
    while n != 1:
       r, m = divmod(n, d)
       if m == 0:
           n = r
           if d not in ldiv:
               ldiv.append(d)
       else:
           d = lprimes[np]

    return ldiv


l =  genlprimes(LIMIT)
print numdivsprimes(l, 999999231)
