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
    LIMITE = 50

    s = 10000000000000
    r = ''

    for n1 in range(1, LIMITE):
        if n1 > s:
            break
        for n2 in range(n1 + 1, LIMITE):
            if n2 > s:
                break
            for n3 in range(n2 + 1, LIMITE):
                if n3 > s:
                    break
                for n4 in range(n3 + 1, LIMITE):
                    if n4 > s:
                        break
                    for n5 in range(n4 + 1, LIMITE):
                        if n5 > s:
                            break
                        for n6 in range(n5 + 1, LIMITE):
                            if n6 > s:
                                break
                            for n7 in range(n6 + 1, LIMITE):
                                if n7 > s:
                                    break
                                p = [n1, n2, n3, n4, n5, n6, n7]
                                if check_S(p):
                                    s1 = sum(p)
                                    if s1 < s:
                                        s = s1
                                        # print(n1, n2, n3, n4, n5, n6, n7)
                                        # ''.join(n1, n2, n3, n4, n5, n6, n7)
                                        r = ''.join(str(x) for x in p)

    return int(r)
