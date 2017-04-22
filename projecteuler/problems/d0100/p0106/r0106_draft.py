# -*- coding: utf-8 -*-

import copy
import itertools

def check_S(values):

    v_ant = []
    v = []
    v_cur = []
    v_ant = copy.deepcopy(values)

    # TODO falta ver si hay elementos repetidos...

    for r in range(2, len(values)):
        for c in itertools.combinations(values, r):
            s = sum(c)
            print('c', c)
            # if s in v or s < max(v_ant) or s in v_ant:
            if s in v:
                print('ERROR-1', s, v_ant)
                return False
            elif  s < max(v_ant):
                print('ERROR-2', s, v_ant)
                return False
            elif s in v_ant:
                print('ERROR-3', s, v_ant)
                return False
            else:
                v.append(s)
                v_cur.append(s)

        v_ant = copy.deepcopy(v_cur)

    print(v)
    return True

def check_S_v2(values):

    v_ant = []
    v = []
    v_cur = []
    v_ant = copy.deepcopy(values)
    t = 0 
    sumun = []

    # TODO falta ver si hay elementos repetidos...

    for r1 in range(1, len(values)):
        for c in itertools.combinations(values, r1):
            # s = sum(c)
            # print('c', c)
            # monto una lista...
            v = []
            for i in values:
                if i not in c:
                    v.append(i)

            # print('PREVIO', c, v)
            for r2 in range(1, len(v) + 1):
                for b in itertools.combinations(v, r2):
                    print(c, b, r2)
                    t += 1
    
                        
    print(t // 2)
    return True

def result():

    # Una solución de 12, obtenida del ejercicio 0105 y que es válida
    S = [20, 31, 38, 39, 40, 42, 45]
    S = [1219, 1183, 1182, 1115, 1035, 1186, 591, 1197, 1167, 887, 1184, 1175]
    S = [3, 5, 6, 7]

    check_S_v2(S)
    # check_S(S)

    return 0
