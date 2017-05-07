# -*- coding: utf-8 -*-


def m(get, exps, step, better):

    yet_tested = []

    if get == 1:
        return 0

    if step > better:
        return better

    # 1. Tenemos que ver como llamarlo :S no lo tengo claro...
    # combinaciones de dos en dos :D
    # for par in list(set(list(itertools.combinations(exps, 2)))):
    for i in exps:
        for j in exps:
            n = i + j
            if n in yet_tested:
                continue
            else:
                yet_tested.append(n)

            if n > get:
                # si ya la suma es major, podemos salir
                return better

            if n == get:
                # Es solucion
                return step

            if n not in exps and step < better and n < get:
                better = m(get, exps + [n], step + 1, better)

    return better


def result():
    STEP = 1
    EXP_TO_GET = 200
    total = 0
    v = 0

    for k in range(1, EXP_TO_GET + 1):
        v = m(k, [1], STEP, v + 1)
        print(k, v)
        total += v

    return total
