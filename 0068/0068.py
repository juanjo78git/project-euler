#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools


def es_solucion_magic5(magic5):
    """ nos indica si un magic5 es solucion """
    sumatorio = sum(magic5[0])
    for linea in magic5:
        if sumatorio != sum(linea):
            return False
    return True


def getlistrestantes(comb):
    a = list(range(1, 11))
    for x in comb:
        a.remove(x)
    return a

def magic5_to_str(magic5):
    m5str = ''

    # falta ordenar en reloj...
    i = 0
    i_min = -1
    v_min = 100
    for x in magic5:
        if x[0] < v_min:
            i_min = i
            v_min = x[0]
        i = i + 1

    magic5ord = magic5[i_min:] + magic5[:i_min]

    for m in magic5ord:
        m5str = m5str + ''.join(str(x) for x in m)
    return m5str


# combinaciones

# asi saco todas las permutaciones posibles del pentagono central
lcomb = list(itertools.permutations(range(1, 11), 5))

soluciones = []

for comb in lcomb:
    magic5 = []
    magic5.append(list([None, comb[0], comb[1]]))
    magic5.append(list([None, comb[1], comb[2]]))
    magic5.append(list([None, comb[2], comb[3]]))
    magic5.append(list([None, comb[3], comb[4]]))
    magic5.append(list([None, comb[4], comb[0]]))

    restantes = getlistrestantes(comb)

    lperm = list(itertools.permutations(restantes, 5))

    for perm in lperm:

        magic5[0][0] = perm[0]
        magic5[1][0] = perm[1]
        magic5[2][0] = perm[2]
        magic5[3][0] = perm[3]
        magic5[4][0] = perm[4]
        
        if es_solucion_magic5(magic5):
            if len(magic5_to_str(magic5)) == 16:
                soluciones.append(magic5_to_str(magic5))

soluciones.sort(reverse=True)
print "Solucion 0068", soluciones[0]
