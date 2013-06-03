# -*- coding: utf-8 -*-

#!/usr/bin/pypy

from datetime import datetime

LIMITE = 100
LIMITE = 1500000


def coprime_odd_even(mo, no, limite):
    """ Generador de coprimos par-impar, impar-par, el limite corresponde
    a m**2 + n**2 """
    ms = [mo] * 3
    ns = [no] * 3
    # rama del arbol
    t = 0
    m = mo
    n = no
    g1 = True
    g2 = True
    g3 = True
    while True:
        yield m, n

        while g1 or g2 or g3:
            if t == 0:
                m = (2 * ms[0]) - ns[0]
                n = ms[0]
                ms[0] = m
                ns[0] = n
                t = 1
                if (m ** 2) + (n ** 2) > limite:
                    g1 = False
                else:
                    break

            elif t == 1:
                m = (2 * ms[1]) + ns[1]
                n = ms[1]
                ms[1] = m
                ns[1] = n
                t = 2
                if (m ** 2) + (n ** 2) > limite:
                    g2 = False
                else:
                    break

            elif t == 2:
                m = ms[2] + (ns[2] * 2)
                n = ns[2]
                ms[2] = m
                ns[2] = n
                t = 0
                if (m ** 2) + (n ** 2) > limite:
                    g3 = False
                else:
                    break


def long_terna_pitagorica(m, n, k):
    """ a partir de un m, n y k devuelve la longitud de un triangulo """
    a = k * ((m ** 2) - (n ** 2))
    b = k * 2 * m * n
    c = k * ((m ** 2) + (n ** 2))
    #if (a + b + c) <= LIMITE:
        #print a, b, c, (a + b + c)
    return a + b + c


# controlamos el tiempo de ejecución
start_time = datetime.now()

# lista para guardar los "L" que encontramos con solución
eles = {}
# total de L
t = 0

co = coprime_odd_even(2, 1, LIMITE)
exit = 0
m = 0
n = 0
m_ant = 0
n_ant = 0

while True:
    # obtenemos una tupla m,n, el generador parará cuando sean iguales a las
    # anteriores
    # TODO: Mejorar con un límite o algo así, que he visto
    m, n = co.next()
    if m == m_ant and n == n_ant:
        break
    else:
        m_ant = m
        n_ant = n

    if m > n:
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
                        print t
                else:
                    eles[l] = 1
                    t += 1
                    print t

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0075: ", t
