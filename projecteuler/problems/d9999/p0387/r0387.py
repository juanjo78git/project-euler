# -*- coding: utf-8 -*-

from projecteuler import mymaths


def _sum_digits_int(n):
    t = 0
    for c in str(n):
        t += int(c)

    return t


def h(n, maxlen, t):
    """ strong, right truncatable Harshad primes """

    len_n = len(str(n))

    if len_n < maxlen + 1:
        if mymaths.isprime(n) and len(str(n)) > 1:
            m = int(str(n)[:-1])
            d = divmod(m, _sum_digits_int(m))
            if mymaths.isprime(d[0]):
                return (t + n)

        if n > 0:
            d = divmod(n, _sum_digits_int(n))

            if d[1] != 0:
                return t

        for i in range(0, 10):
            if n == 0 and i == 0:
                continue
            new_n = int(str(n) + str(i))
            t = h(new_n, maxlen, t)
    return t


def result():
    t = 0

    # 2^LIMITE
    LIMITE = 14

    t = h(0, LIMITE, 0)

    return t
