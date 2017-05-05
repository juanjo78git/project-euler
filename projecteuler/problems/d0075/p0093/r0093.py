# -*- coding: utf-8 -*-

from __future__ import division
import itertools

# añadimos la propiedad asociativa, así generaremos muchas menos combinaciones,
# por ejemplo para el caso de + + + automáticamente se calculará como
# a b c d + + +
# de igual forma para + y - y para multiplicaciones.
#
# 20130705: tengo una idea, consiste en buscar por un número dado si existe,
#           sería ver si por ejemplo se puede formar el número 1, en caso
#           correcto se lanzaría para el número 2 y así sucesivamente.. pero
#           claro, necesitamos una función rápida para verificar esto...
# 20160204: cansado de probar fuerza bruta, busqué que valores eran el
#           resultado (que no cómo lo resolvía) y vi que eran valores menos que
#           10! asi que saqué dos conclusiones:
#               1. no se leer, ya que el ejercicio dice DIGITOS, y DIGITOS son
#                  números de menos de 10, tonto!
#               2. no dice que las divisiones tengan que ser exactas, pueden
#                  devolver 0.5 que al multiplicar por otro valor devuelve un
#                  número exacto
#           tras VER eso, me dí cuenta que el ejercicio YA estaba resuelto


def calc_valores_parent(comb_dig_opers):
    ''' recupera todos los posibles resultados con 4 números y 3 operadoers '''
    l = []

    a = str(comb_dig_opers[0])
    b = str(comb_dig_opers[1])
    c = str(comb_dig_opers[2])
    d = str(comb_dig_opers[3])
    op1 = str(comb_dig_opers[4])
    op2 = str(comb_dig_opers[5])
    op3 = str(comb_dig_opers[6])

    # todas las posibles combinaciones de paréntesis
    s01 = a + op1 + b + op2 + c + op3 + d
    s02 = '(' + a + op1 + b + ')' + op2 + c + op3 + d
    s03 = a + op1 + '(' + b + op2 + c + ')' + op3 + d
    s04 = a + op1 + b + op2 + '(' + c + op3 + d + ')'
    s05 = '(' + a + op1 + b + op2 + c + ')' + op3 + d
    s06 = a + op1 + '(' + b + op2 + c + op3 + d + ')'
    s07 = '(' + a + op1 + b + ')' + op2 + '(' + c + op3 + d + ')'
    s08 = '((' + a + op1 + b + ')' + op2 + c + ')' + op3 + d
    s09 = a + op1 + '(' + b + op2 + '(' + c + op3 + d + '))'
    s10 = '(' + a + op1 + '(' + b + op2 + c + '))' + op3 + d
    s11 = a + op1 + '((' + b + op2 + c + ')' + op3 + d + ')'

    s = [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11]

    for si in s:
        try:
            r = eval(si)
            if int(r) == r:
                if r not in l and r > 0:
                    l.append(r)
        except NameError:
            pass
        except ZeroDivisionError:
            pass

    return l


def get_comb_numeros_operadores(dig):
    """ devuelve una lista de numeros y operadores """
    normal = []
    # para cada union de 3 operadores...
    for op in list(itertools.product('+-*/', repeat=3)):

        for per in list(itertools.permutations('0123', 4)):
            nrm = []
            for i in per:
                nrm.append(dig[int(i)])

            nrm.append(op[0])
            nrm.append(op[1])
            nrm.append(op[2])

            normal.append(nrm)

    return normal


def get_max_sequence_valor(valores):
    sr = sorted(valores)

    n = 1
    for j in sr:
        if n != int(j):
            break
        n = n + 1

    return (n - 1)


def calc_0093():
    maximo = 0
    max_digits = [0, 0, 0, 0]
    for digits in itertools.combinations(range(1, 10), 4):

        combs_dig_opers = get_comb_numeros_operadores(digits)

        all_valores = []

        for comb_dig_opers in combs_dig_opers:
            valores = calc_valores_parent(comb_dig_opers)

            # añadimos los valores calculados que no estén en "r"
            for valor in valores:
                if valor not in all_valores:
                    all_valores.append(valor)

        # print all_valores
        max_actual = get_max_sequence_valor(all_valores)

        if maximo < max_actual:
            # print 'Maximo: ', n - 1, ' -- con valores: ', f
            maximo = max_actual
            max_digits = digits

    return max_digits


def result():

    resultado = calc_0093()

    # print "Resultado de 0093: " + ''.join(str(r) for r in resultado)
    return int(''.join(str(r) for r in resultado))
