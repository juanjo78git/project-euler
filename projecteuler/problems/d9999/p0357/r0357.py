# -*- coding: utf-8 -*-

# Consider the divisors of 30: 1,2,3,5,6,10,15,30.
# It can be seen that for every divisor d of 30, d+30/d is prime.

# Find the sum of all positive integers n not exceeding 100 000 000
# such that for every divisor d of n, d+n/d is prime.

###############################################################################

import random


def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    # for i in xrange(s-1):
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def miller_rabin(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    # for repeat in xrange(20):
    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True


# es un número primo
def isprime(n):
    if n == 1:
        return False

    # rango empieza en 2, y solo tenemos que llegar hasta el cuadrado de n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False

    return True


def isnumdivprimes(n):

    # por cada divisor por debajo de la raiz hay uno por encima, luego
    # los divisores serían d y n/d
    limite = int(n**0.5)

    # caso primero de n como divisor de si mismo o 1 es divisor de si mismo
    if not isprime(n+1):
        return False

    if limite*limite == n:
        return False

    for d in range(2, limite + 1):

        di, m = divmod(n, d)
        if m == 0:
            # explicacion, si existe algun divisor dos veces, no cumple
            if di % d == 0:
                return False

            p = d + di

            # if not isprime(p):
            if not miller_rabin(p):
                return False
    return True


def result():
    rango = 100000000

    # 1 cumple, lo ponemos a mano
    total = 1

    # solo tratamos los pares
    for n in range(2, rango + 1, 2):

        # if n % 100000 == 0:
        #     print (100*n)/float(rango)

        if isnumdivprimes(n):
            total = total + n

    # print("Resultado para 0357:", total)
    return total
