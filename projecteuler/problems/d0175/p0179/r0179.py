# -*- coding: utf-8 -*-

from projecteuler import mymaths


def result():
    # 10^7
    LIMIT = 10000000

    nd_ant = 0
    total = 0
    for n in range(2, LIMIT):
        nd = mymaths.numdivs(n)
        # if n % 100000 == 0:
        #     print n
        if nd == nd_ant:
            total += 1
        nd_ant = nd

    # print "Resultado de 0179: ", total
    return total
