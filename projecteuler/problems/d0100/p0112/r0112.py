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


def is_bouncy(n):
    """ devuelve si es de tipo variable (bouncy en ingles) """
    decreciente = False
    creciente = False
    c_ant = None

    if len(str(n)) == 1:
        return False

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
                return True

        elif decreciente:
            if c_ant < c:
                return True

        c_ant = c

    return False


def percent_bouncy(p):
    """ obtiene el bouncy que es mayor o igual a p """
    n = 1
    t = 0
    while True:
        if is_bouncy(n):
            t += 1

        if ((t / float(n)) * 100) >= p:
            print n
            return

        n += 1


def result():
    # print "Resultado 0112: ", percent_bouncy(99)
    return percent_bouncy(99)
