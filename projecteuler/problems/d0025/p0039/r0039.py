# -*- coding: utf-8 -*-


def es_solucion(a, b, p):

    pcalc = a + b + (a**2 + b**2)**0.5

    if (pcalc == p):
        return True

    return False


def result():
    maxp = 0
    total = 0
    max_total = 0

    N = 1000

    # for p in range(1, N-(N//2)):
    for p in range(1, N):

        total = 0

        for a in range(1, 1001):

            for b in range(a+1, 1001):

                if a + b > p:
                    break

                if es_solucion(a, b, p):
                    #print(a, b, p)
                    total = total + 1

                    if (max_total < total):
                        maxp = p
                        max_total = total
                        # print("total", maxp, max_total, p, a, b)
    return maxp
