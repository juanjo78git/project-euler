# -*- coding: utf-8 -*-

import copy
import itertools

def check_S(values):
    """ 
    Chequea si es S:
        1. S(B) != S(C), siendo B y C subconjuntos de A
        2. Si B tiene más elementos que C entonces S(B) > S(C)
    """
    
    saco = []
    saco_ant = []

    for h in range(0, len(values)):
        v0 = values[h:]
        print('v0', v0)

        for i in range(1, len(v0)):
            print(v0[0:i])
            print(v0[i:])
            v1 = v0[0:i]
            v2 = v0[i:]

            for k in range(0, len(v2)):
                s1 = sum(v1)
                s2 = v2[k]
                print(s1, s2)
                t = s1 + s2
                if t in saco:
                    return False
                else:
                    saco.append(t)

    print(saco)
    return True

def check_S_v3(values):

    for size in range(1, len(values)):
        for offset in range(0, len(values)):
            if offset + size > len(values):
                continue
            # print(size, offset, values[offset:offset + size])
            # print(comb(values, values[offset:offset + size]))
            offset_values = values[offset:offset + size]
            exit, v1 = comb(values, offset_values)
            print(offset_values, v1)



def comb(values, subvalues):
    """ """
    summun = []
    rest = []

    for v in values:
        if v not in subvalues and v > min(subvalues):
            rest.append(v)

    for r in rest:
        s = sum(subvalues) + r
        if s in summun:
            # print('Error', s, summun)
            return False, summun
        else:
            summun.append(s)

    return True, summun


def check_S_v2(values):
    """ 
    Chequea si es S:
        1. S(B) != S(C), siendo B y C subconjuntos de A
        2. Si B tiene más elementos que C entonces S(B) > S(C)
    """
    
    saco = []
    saco_ant = copy.deepcopy(values)

    for k in range(0, len(values)):
        print('kkkkkkkkkkk', k)

        saco_curr = []

        for m in range(0, len(values)):

            for h in range(k, len(values)):
                if m > k:
                    continue
                v0 = values[h:]
                # print('v0', v0)
                # print(values[0:h + 1])
                # s1 = sum(values[0:h + 1])
                print('s1', values[h + m], values[m:k + m], m, k)
                s1 = values[h + m] + sum(values[m:k + m])

                for i in range(1, len(v0) - m):
                    s2 = v0[i + m]
                    print(s1, s2)
                    t = s1 + s2
                    # print('saco_ant', saco_ant)
                    # print('t', t)
                    if t in saco or t < max(saco_ant) or t in saco_ant:
                        print(t, saco, max(saco_ant), saco_ant)
                        return False
                    else:
                        saco.append(t)
                        saco_curr.append(t)

            saco_ant = copy.deepcopy(saco_curr)

    print(saco)
    return True


def check_S_v4(values):

    v_ant = []
    v = []
    v_cur = []
    v_ant = copy.deepcopy(values)

    # TODO falta ver si hay elementos repetidos...

    for r in range(2, len(values)):
        for c in itertools.combinations(values, r):
            s = sum(c)
            if s in v or s < max(v_ant) or s in v_ant:
                print('ERROR', s, v_ant)
                return False
            else:
                v.append(s)
                v_cur.append(s)

        v_ant = copy.deepcopy(v_cur)

    # print(v)
    return True


def result():
    # check_S()
    # if check_S_v2([11, 18, 19, 20, 22, 25]):
    # if check_S_v2([2, 3, 15]):
    l = [81, 88, 75, 42, 87, 84, 86, 65]
    # l = [11, 18, 19, 20, 22, 25]
    l = [2, 3, 15]
    l = [157, 150, 164, 119, 79, 159, 161, 139, 158]
    l.sort()
    if check_S_v4(l):
        print('True')
    else:
        print('False')

    return 0
