# -*- coding: utf-8 -*-

from projecteuler import mymaths


def genlistprimeslimit(LIMIT):
    l = []
    genp = mymaths.prime()
    while True:
        p = genp.next()
        if p < ((LIMIT // 2) + 1):
            l.append(p)
        else:
            break
    return l


def result():
    LIMIT = 100000000
    primes = genlistprimeslimit(LIMIT)
    # print "Lista de primos generada, con %d elementos" % len(primes)
    composites = []

    for i in range(0, len(primes)):
            for j in range(i, len(primes)):
                c = primes[i] * primes[j]
                if c < LIMIT:
                    composites.append(primes[i] * primes[j])
                else:
                    break

    # print primes
    # print composites
    # print len(composites)

    # print "Resultado de 0187: ", len(composites)
    return len(composites)
