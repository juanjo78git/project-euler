# -*- coding: utf-8 -*-

import copy
import itertools
import os


def check_S(values):

    v_ant = []
    v = []
    v_cur = []
    v_ant = copy.deepcopy(values)

    # TODO falta ver si hay elementos repetidos...

    for r in range(2, len(values)):
        for c in itertools.combinations(values, r):
            s = sum(c)
            if s in v or s < max(v_ant) or s in v_ant:
                # print('ERROR', s, v_ant)
                return False
            else:
                v.append(s)
                v_cur.append(s)

        v_ant = copy.deepcopy(v_cur)

    # print(v)
    return True


def result():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    fichero = os.path.join(ROOT_DIR, 'p105_sets.txt')

    t = 0

    f = open(fichero, 'r')

    for linea in f:
        v = []
        z = linea.replace('\n', '').split(',')
        for i in z:
            v.append(int(i))
        v.sort()
        if check_S(v):
            t += sum(v)
    f.close()

    return t
