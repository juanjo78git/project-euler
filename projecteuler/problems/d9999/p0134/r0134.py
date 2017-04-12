# -*- coding: utf-8 -*-

# Project Euler: 134 Consider the consecutive primes p1 = 19 and p2 = 23. It
# can be verified that 1219 is the smallest number such that the last digits
# are formed by p1 whilst also being divisible by p2.
#
# In fact, with the exception of p1 = 3 and p2 = 5, for every pair of
# consecutive primes, p2 > p1, there exist values of n for which the last
# digits are formed by p1 and n is divisible by p2. Let S be the smallest of
# these values of n.
#
# Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.

from projecteuler import mymaths


def calcula_s(p1, p2):

    n = 1

    while True:
        test = int(str(n) + str(p1))

        if divmod(test, p2)[1] == 0:
            return test

        n += 1


def result():

    LIMITE = 1000000
    # LIMITE = 100
    total = 0

    # Genera unos 70 mil
    primos = mymaths.genprimes(5, LIMITE)

    for i in range(0, len(primos) - 1):
        p1 = primos[i]
        p2 = primos[i + 1]
        s = calcula_s(p1, p2)
        print(p1, p2, s)
        total += s

    return total
