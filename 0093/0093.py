#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools



def p93(a, b, c, d):
    pos_rpns = []
    # para cada union de 3 operadores...
    for op in list(itertools.combinations_with_replacement('+-*/', 3)):
        elements = str(a) + str(b) + str(c) + str(d) + "".join(op)
        for pos_rpn in list(itertools.permutations(elements, 7)):
            #if pos_rpn[0] >= '0' and pos_rpn[0] <= '9':
            res = ''
            for i in pos_rpn:
                res = res + i + ' '
            pos_rpns.append(res)
    
    return pos_rpns



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


MAX = 120

def p93_3():
    maximo = 0
    for a in range(1, MAX):
        print a
        for b in range(a + 1, MAX):
            for c in range(b + 1, MAX):
                for d in range(c + 1, MAX):
                    l = p93(a, b, c, d)
                    
                    r = []

                    for i in l:
                        try:
                            p = polish_eval(i)
                            if p > 0:
                                if p not in r:
                                    r.append(p)
                        except:
                            z = 0

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

p93_3()
