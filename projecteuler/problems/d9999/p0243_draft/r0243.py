# -*- coding: utf-8 -*-

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


from projeceuler import mymaths


def R_mayor(n, d, min_n, min_d):
    """ está claro que si llegamos a un punto donde ya es mayor, mejor nos
        olvidamos, no vamos a poder sacar ese número """
    return (min_d * n) >= ((d - 1) * min_n)


def result():
    # LIMITE = 10000000
    RANGO = 10000000

    min_d = 94744
    min_n = 15499
    # min_d = 10
    # min_n = 4
    d = 30

    p = mymaths.prime()

    # while True:
    #     if p.next() == 5:
    #         break

    mymin = 0.1856
    mini = 0
    z = 0

    d = p.next()
    d = p.next()
    d = p.next()

    d = 20550002

    # print min_n / float(min_d)
    nomas = False

    while True:
        # d = p.next() + 1
        d += 1
        z += 1

        # if z % 10000 == 0:
        #     print d

        noreducibles = mymaths.euler_phi(d)

        # vemos si es posible que sea solucion
        if not R_mayor(noreducibles, d, min_n, min_d):
            break

        mini = noreducibles / float(d - 1)
        if mini < mymin:
            mymin = mini
            mini
            if mini > 0.165:
                # print noreducibles, d - 1, mini
                if not nomas:
                    d += RANGO
            else:
                d -= RANGO
                nomas = True
            # print noreducibles, d, mymaths.numdivsprimes(d)

    # si salimos es que tenemos solucion...
    # print "Resultado de 243: ", d
    return d
