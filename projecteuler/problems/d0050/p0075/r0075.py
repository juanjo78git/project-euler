# -*- coding: utf-8 -*-

import math

#LIMITE = 700


# recursivo
#

def all_coprime(m, n, limit, l):
    mlimit = int(math.sqrt(limit / 2.0))

    if m == 2 and n == 1:
        l.append([m, n])

    # rama 1
    m_next = (2 * m) - n
    n_next = m
    if m_next <= mlimit:
        l.append([m_next, n_next])
        l = all_coprime(m_next, n_next, limit, l)

    # rama 2
    m_next = (2 * m) + n
    n_next = m
    if m_next <= mlimit:
        l.append([m_next, n_next])
        l = all_coprime(m_next, n_next, limit, l)

    # rama 3
    m_next = m + (n * 2)
    n_next = n
    if m_next <= mlimit:
        l.append([m_next, n_next])
        l = all_coprime(m_next, n_next, limit, l)

    return l


def long_terna_pitagorica(m, n, k):
    """ a partir de un m, n y k devuelve la longitud de un triangulo """
    a = k * ((m ** 2) - (n ** 2))
    b = k * 2 * m * n
    c = k * ((m ** 2) + (n ** 2))
    #if (a + b + c) <= LIMITE:
        #print a, b, c, (a + b + c)
    return a + b + c


def result():
    LIMITE = 1500000

    # lista para guardar los "L" que encontramos con solución
    eles = {}
    # total de L
    t = 0

    # generamos todas las parejas de coprimos...
    all_cop = all_coprime(2, 1, LIMITE, [])

    for cop in all_cop:
        m = cop[0]
        n = cop[1]
        for k in range(1, LIMITE):
            l = long_terna_pitagorica(m, n, k)
            if l > LIMITE:
                break
            else:
                if l in eles:
                    # solo restamos una vez el elemento que está, imagina que
                    # llega una l por tercera vez, restaríamos demasiados!
                    if eles[l] == 1:
                        t -= 1
                        eles[l] = 2
                else:
                    eles[l] = 1
                    t += 1

    # print "Resultado de 0075: ", t
    return t
