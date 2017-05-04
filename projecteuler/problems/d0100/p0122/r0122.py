# -*- coding: utf-8 -*-

import itertools


def m(get, exps, step, better):

    # print(get, exps, step, better)
    # print(get, step, better)

    if step > better:
        return better

    # 1. Tenemos que ver como llamarlo :S no lo tengo claro...

    # combinaciones de dos en dos :D
    for par in list(set(list(itertools.combinations(exps, 2)))): 

        n = sum(par)

        if n == get:
            # Es solucion
            # print('Solucion:', par, step, set(exps))
            return step

        if sum(par) not in exps and step < better and sum(par) < get:
            # añadimos dos veces el mismo numero
            # exps.append(sum(par))
            # exps.append(sum(par))
            
            better = m(get, exps + [n, n], step + 1, better)

    return better


def result():
    # por definicion al inicio, el mejor será 15

    BETTER = 15
    STEP = 1
    EXP_TO_GET = 15
    total = 0

    # b = m(EXP_TO_GET, [1, 1], STEP, BETTER)
    # for exp_to_get in range(1, 200 + 1):
    #     total += m(exp_to_get, [1, 1], 1, EXP_TO_GET)
    #     print(exp_to_get)

    total = m(200, [1, 1], 1, 20)
    return total
