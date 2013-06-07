# -*- coding: utf-8 -*-

#!/usr/bin/pypy

from datetime import datetime

DIVISOR = 1000000


def pentagonal(n):
    """ el termino n es dado por (3n^2-n)/2 """
    return ((n * (3 * n - 1)) / 2)


def generalised_pentagonal(n):
    """ dependiendo de si es par o impar """
    if n % 2 == 0:
        return pentagonal((n / 2) + 1)
    else:
        return pentagonal(-(n / 2) - 1)


def termsign(i):
    if i % 4 < 2:
        # add if i mod 4 is 0 or 1
        return 1
    else:
        # subtract otherwise
        return -1


# controlamos el tiempo de ejecución
start_time = datetime.now()

pt = [1]
n = 0
while True:
    n += 1
    r = 0
    i = 0
    while True:
        k = generalised_pentagonal(i)
        if k > n:
            break
        r += termsign(i) * pt[n - k]
        i += 1
    pt.append(r)
    if r % DIVISOR == 0:
        break

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0078: ", n
