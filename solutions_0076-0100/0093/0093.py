#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools
import operator

# añadimos la propiedad asociativa, así generaremos muchas menos combinaciones,
# por ejemplo para el caso de + + + automáticamente se calculará como
# a b c d + + +
# de igual forma para + y - y para multiplicaciones.

# 20130705: tengo una idea, consiste en buscar por un número dado si existe,
#           sería ver si por ejemplo se puede formar el número 1, en caso
#           correcto se lanzaría para el número 2 y así sucesivamente.. pero
#           claro, necesitamos una función rápida para verificar esto...


def resultados(ia, ib, ic, id, op1, op2, op3):
    ''' entramos sin no asociativa... '''
    l = [0]

    a = str(ia)
    b = str(ib)
    c = str(ic)
    d = str(id)

    s1 = a + op1 + b + op2 + c + op3 + d
    s2 = '(' + a + op1 + b + ')' + op2 + c + op3 + d
    s3 = a + op1 + '(' + b + op2 + c + ')' + op3 + d
    s4 = a + op1 + b + op2 + '(' + c + op3 + d + ')'
    s5 = '(' + a + op1 + b + op2 + c + ')' + op3 + d
    s6 = a + op1 + '(' + b + op2 + c + op3 + d + ')'
    s7 = '(' + a + op1 + b + ')' + op2 + '(' + c + op3 + d + ')'
    s8 = '((' + a + op1 + b + ')' + op2 + c + ')' + op3 + d
    s9 = a + op1 + '(' + b + op2 + '(' + c + op3 + d + '))'
    s10 = '(' + a + op1 + '(' + b + op2 + c + '))' + op3 + d
    s11 = a + op1 + '((' + b + op2 + c + ')' + op3 + d + ')'

    s = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11]

    for si in s:
        try:
            r = eval(si)
            if r not in l and r > 0:
                l.append(r)
        except:
            #z = 0
            pass

    return l


def asociativa(op):
    if op[0] in ('-', '+') and op[1] in ('+', '-') and op[2] in ('+', '-'):
        return True
    else:
        if op[0] in ('*') and op[1] in ('*') and op[2] in ('*'):
            return True

    return False


def rpnvalid(rpn):

    if not rpn[0].isdigit():
        return False

    if rpn[6].isdigit():
        return False

    if not rpn[1].isdigit() and not rpn[2].isdigit():
        return False

    if rpn[3].isdigit() and rpn[4].isdigit() and rpn[5].isdigit():
        return False

    return True


def p93(a, b, c, d):
    pos_rpns = []
    # para cada union de 3 operadores...
    #element = str(a) + str(b) + str(c) + str(d)
    for op in list(itertools.combinations_with_replacement('+-*/', 3)):

        elem = [a, b, c, d, op[0], op[1], op[2]]

        if asociativa(op):
            #pos_rpn2.append(op[0])
            #pos_rpn2.append(op[1])
            #pos_rpn2.append(op[2])
            pos_rpns.append(elem)
        else:
            for per in list(itertools.permutations('0123456', 7)):
                rpn = []
                for i in per:
                    # a ver, i sería la convinación 0123456
                    rpn.append(str(elem[int(i)]))

                if rpnvalid(rpn):
                    pos_rpns.append(rpn)

    return pos_rpns


def p93_normal(a, b, c, d):
    normal = []
    # para cada union de 3 operadores...
    element = [a, b, c, d]
    for op in list(itertools.product('+-*/', repeat=3)):

        elem = [a, b, c, d, op[0], op[1], op[2]]

        if asociativa(op):
            #pos_rpn2.append(op[0])
            #pos_rpn2.append(op[1])
            #pos_rpn2.append(op[2])
            normal.append(elem)
        else:
            for per in list(itertools.permutations('0123', 4)):
                nrm = []
                for i in per:
                    nrm.append(element[int(i)])

                nrm.append(op[0])
                nrm.append(op[1])
                nrm.append(op[2])

                normal.append(nrm)

    return normal

# rpn calculadora...
operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}


def polish_eval(expression):
    elements = expression.split()
    pile = []
    while elements:
        e = elements.pop(0)
        if e in operators:
            b = pile.pop()
            a = pile.pop()
            pile.append(operators[e](a, b))
        else:
            pile.append(int(e))
    return pile[0]

ARITHMETIC_OPERATORS = {
    '+':  operator.add, '-':  operator.sub,
    '*':  operator.mul, '/':  operator.div,
}


def postfix(expression, operators=ARITHMETIC_OPERATORS):
    stack = []
    #for val in expression.split():
    for val in expression:
        if val in operators:
            f = operators[val]
            stack[-2:] = [f(*stack[-2:])]
        else:
            stack.append(int(val))
    return stack.pop()


MAX = 75
INIT = 1


def p93_3():
    maximo = 0
    for a in range(INIT, MAX):
        print a
        for b in range(a + 1, MAX):
            print b
            for c in range(b + 1, MAX):
                for d in range(c + 1, MAX):
                    l = []
                    l = p93(a, b, c, d)

                    r = []

                    for i in l:
                        try:
                            p = postfix(i)
                            if p > 0:
                                if p not in r:
                                    r.append(p)
                        except:
                            #z = 0
                            pass
                            #print i

                    # una vez llegados aqui tenemos una lista de los valores
                    # que hemos ido obteniendo, la pintamos de primeras...
                    sr = sorted(r)

                    n = 1
                    for j in sr:
                        if n != int(j):
                            break
                        n = n + 1

                    if maximo < n - 1:
                        print n - 1, a, b, c, d
                        maximo = n - 1


def p93_3_normal():
    maximo = 0
    for a in range(INIT, MAX):
        print a
        for b in range(a + 1, MAX):
            print b
            for c in range(b + 1, MAX):
                for d in range(c + 1, MAX):
                    l = []
                    l = p93_normal(a, b, c, d)

                    r = []

                    for i in l:
                        p = resultados(i[0], i[1], i[2], i[3], i[4], i[5],
                                       i[6])
                        for pi in p:
                            if pi > 0:
                                if pi not in r:
                                    r.append(pi)

                    # una vez llegados aqui tenemos una lista de los valores
                    # que hemos ido obteniendo, la pintamos de primeras...
                    sr = sorted(r)

                    n = 1
                    for j in sr:
                        if n != int(j):
                            break
                        n = n + 1

                    if maximo < n - 1:
                        print n - 1, a, b, c, d
                        maximo = n - 1

#p93_3_normal()
p93_3()
