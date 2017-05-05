# -*- coding: utf-8 -*-

import itertools


def m(get, exps, step, better):

    # print(get, exps, step, better)
    # print(get, step, better)
    yet_tested = []

    if step > better:
        return better

    # 1. Tenemos que ver como llamarlo :S no lo tengo claro...

    # combinaciones de dos en dos :D
    for par in list(set(list(itertools.combinations(exps, 2)))): 


        n = sum(par)
        
        if n in yet_tested:
            continue
        else:
            yet_tested.append(n)

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


def m2(get, exps, step, better):

    yet_tested = []
    # print(get, exps, len(exps), step, better)
    # print(get, step, better)
    # exps.sort()

    if step > better:
        return better

    # 1. Tenemos que ver como llamarlo :S no lo tengo claro...

    # combinaciones de dos en dos :D
    # for par in list(set(list(itertools.combinations(exps, 2)))): 
    for i in exps:
        for j in exps:
            n = i + j
            if n in yet_tested:
                # return better
                continue
            else:
                yet_tested.append(n)

            if n > get:
                # break
                # si ya la suma es major, podemos salir
                return better

            # n = sum(par)

            if n == get:
                # Es solucion
                # print('Solucion:', par, step, set(exps))
                return step

            if n not in exps and step < better and n < get:
                # añadimos dos veces el mismo numero
                # exps.append(sum(par))
                # exps.append(sum(par))
                
                better = m2(get, exps + [n], step + 1, better)

    return better


def result():
    # por definicion al inicio, el mejor será 15

    BETTER = 15
    STEP = 1
    EXP_TO_GET = 200
    total = 0
    total2 = 0

    # b = m(EXP_TO_GET, [1, 1], STEP, BETTER)
    # for exp_to_get in range(1, EXP_TO_GET + 1):
    #     total = m(exp_to_get, [1, 1], 1, (exp_to_get // 2) + 5)
    #     # total2 = m2(exp_to_get, [1], 1, exp_to_get)
    #     print(exp_to_get, total, total2, bin(exp_to_get))

    total = m(200, [1, 1], 1, 110)
    # total = m(50, [1, 1], 1, 50)
    # total = m2(50, [1], 1, 50)
    return total
