# -*- coding: utf-8 -*-

# Leyendo un número de izquierda a derecha, si no hay dígitos que se vean
# superados por el dígito a su izquierda, se le denomina un creciente, por
# ejemplo, 134468.
#
# Del mismo modo, si ningún dígito es superado por los dígitos a la derecha, se
# denomina un número decreciente, por ejemplo, 66420.
#
# Vamos a denominar a un entero positivo que no crece ni decrece un número
# "variable", por ejemplo, 155349.
#
# Es evidente que no puede haber números variables inferiores a cien; sin
# embargo, algo más de la mitad de los números inferiores a mil (525) son
# variables. De hecho, el menor número para el que la proporción de números
# variables alcanza por primera vez 50% es 538.
#
# Curiosamente, los números variables son cada vez más comunes, y, para cuando
# llegan a 21780, su proporción es del 90%.
#
# Halla el menor número para el que la proporción de números variables es
# exactamente del 99%.


def b(n):
    """ funciona """
    return n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5)*(n+6)*(n+7)*(n+8)//math.factorial(9)


def is_bouncy(n):
    """ devuelve si es de tipo variable (bouncy en ingles) """
    decreciente = False
    creciente = False
    c_ant = None

    if len(str(n)) == 1:
        return False, 2

    p = str(n)
    a = p[0]

    if len(p.replace(a, '')) == 0:
        return False, 2

    for c in str(n):

        if c_ant is None:
            c_ant = c
            continue

        if c_ant == c:
            continue

        if not decreciente and not creciente:
            if c_ant < c:
                creciente = True
            elif c_ant > c:
                decreciente = True

        elif creciente:
            if c_ant > c:
                return True, 0

        elif decreciente:
            if c_ant < c:
                return True, 0

        c_ant = c

    if decreciente:
        return False, 1
    else:
        return False, 2


def result():
    # for exp in range(1, 10):
    #     t = 0
    #     for i in range(1, 10 ** exp):
    #         if not is_bouncy(i):
    #             print(i)
    #             t += 1

    #     print(10 ** exp, t)

    t = 0
    mode = 0
    b = True
    for i in range(1, 1000):
        b, mode = is_bouncy(i)
        if not b:
            # if mode == 1:
            #     print(mode, "%04d" % i)
            print(mode, len(str(i)), "%03d" % i)
            t += 1
    return t
