# -*- coding: utf-8 -*-

# By replacing the 1st digit of *3, it turns out that six of the nine possible
# values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this
# 5-digit number is the first example having seven primes among the ten
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
# 56773, and 56993. Consequently 56003, being the first member of this family,
# is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an eight prime
# value family.


import itertools


# es un número primo
def isprime(n):
    if n == 1 or n == 0:
        return False
    # rango empieza en 2, y solo tenemos que llegar hasta el cuadrado de n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def nextprime(n):
    while not isprime(n+1):
        n = n + 1
    return n + 1


# el número y la lista de posiciones a cambiar
def replaceprime(n, lpos):
    s = str(n)
    nprimos = 0
    minprimo = -1
    for d in range(0, 10):
        for i in range(0, len(lpos)):
            li = lpos[i]

            # s[li] = str(d) <-- no se puede hacer en python!! :S
            s = s[0:li] + str(d) + s[li+1:]
            t = int(s)

        if isprime(t) and len(str(n)) == len(str(t)):
            nprimos = nprimos + 1
            if t < minprimo or minprimo == -1:
                minprimo = t

    return nprimos, minprimo


def maxreplaceprime(n):
    # listado de posiciones
    lposiciones = [x for x in range(0, len(str(n)))]

    maxnprimes = 0
    for ndigits in range(1, len(str(n))-1):
        llcomb = list(itertools.combinations(lposiciones, ndigits))

        for lcomb in llcomb:
            nprimes, minprimo = replaceprime(n, lcomb)
            if nprimes == 8:
                # print("Resultado es:", minprimo)
                # return 8
                return minprimo

            if nprimes > maxnprimes:
                maxnprimes = nprimes

    return None


def result():
    n = 2
    # nprimes = 8
    r = None

    while r is None:
        r = maxreplaceprime(n)
        n = nextprime(n)

    return r
