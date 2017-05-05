# -*- coding: utf-8 -*-

import math


def A011900():
    """ Generador de cuadrados """
    # Con bastante trampa: https://oeis.org/A011900
    # a(n) = 6*a(n-1) - a(n-2) - 2 with a(0) = 1, a(1) = 3.
    a_0 = 1
    a_1 = 3
    a_t = 0
    while True:
        yield a_1
        a_t = a_1
        a_1 = 6*(a_1) - a_0 - 2
        a_0 = a_t


def get_total_for_blues(blues):

    # resolvemos la ecuacion
    tmp_1 = blues * (blues - 1) * 2
    tmp_2 = (tmp_1 * 4) + 1
    tmp_3 = math.sqrt(tmp_2) + 1
    return tmp_3 / 2


def result():
    n = A011900()

    blues = n.__next__()

    while True:

        total = get_total_for_blues(blues)

        if total > 1000000000000:
            # print "Solucion 0100:", blues
            return blues

        blues = n.__next__()
