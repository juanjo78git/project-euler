# -*- coding: utf-8 -*-

#Consider the fraction, n/d, where n and d are positive integers. If nd and
#HCF(n,d)=1, it is called a reduced proper fraction.

#If we list the set of reduced proper fractions for d  8 in ascending order of
#size, we get:

#1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
#5/7, 3/4, 4/5, 5/6, 6/7, 7/8

#It can be seen that 2/5 is the fraction immediately to the left of 3/7.

#By listing the set of reduced proper fractions for d  1,000,000 in ascending
#order of size, find the numerator of the fraction immediately to the left
#of 3/7.


def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


def mcd_it(a, b):
    while b != 0:
        aux = b
        b = a % b
        a = aux
    return a


def result():
    d_fix = 7
    n_fix = 3
    d_ant = 1000000
    n_ant = 1
    limite = 1000000

    # n/d
    for d in range(1, limite+1):

        n_calc, m = divmod(n_fix*d, d_fix)

        if m == 0:
            continue

        for n in range(n_calc, 0, -1):

            if mcd_it(n, d) == 1:

                if (n*d_ant) > (d*n_ant):
                    d_ant = d
                    n_ant = n
                else:
                    break

    # print("Resultado 0071", n_ant)
    return n_ant
