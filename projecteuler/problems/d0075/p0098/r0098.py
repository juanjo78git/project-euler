# -*- coding: utf-8 -*-

import os


def getdicsquares(maximo):
    """ mete los cuadrados en un diccionario por longitud """
    d = {}

    # generamos el diccionario
    for i in range(1, maximo + 1):
        d[i] = []

    n = 1
    square = n ** 2
    lensquare = len(str(square))
    while lensquare <= maximo:
        if lensquare in d:
            d[lensquare].append(square)
        else:
            d[lensquare] = [square]

        n = n + 1
        square = n ** 2
        lensquare = len(str(square))
        # print square

    return d


def readdictsword(f):
    """ lee un fichero y lo mete en un diccionario """
    dw = {}
    f = open(f, 'r')
    words = f.readline().replace('"', '').replace('\n', '').split(',')
    for w in words:
        if len(w) in dw:
            dw[len(w)].append(w)
        else:
            dw[len(w)] = [w]

        # print w

    return dw


def getrelation(w, n):
    """ devuelve true o false si es una posible relación ya demás un
        diccionario con las relaciones en el caso que sea true """
    ni = 0
    d = {}
    for wi in w:
        nv = int(str(n)[ni])

        # si está la letra en el diccionario con otro valor
        if wi in d:
            if d[wi] != nv:
                return False, {}
        else:
            if nv in d.values():
                return False, {}
            else:
                d[wi] = nv

        ni += 1
    return True, d


def es_anagrama(w1, w2):
    return sorted(list(w1)) == sorted(list(w2))


def get_anagrames(dw, w):
    """ a partir de un diccionario de palabras y de cuadrados, vemos si hay
        más palabras que son anagramas a w y que además sea válido """
    l = dw[len(w)]
    la = []
    for wa in l:
        if wa != w and es_anagrama(wa, w):
            la.append(wa)
    return la


def es_posible_resultado(la, relation, squares):

    maximo = 0
    n = ''
    # primero vamos por cada una de la palabras viendo los números
    for a in la:
        for l in list(a):
            n += str(relation[l])

        if int(n) in squares:
            if maximo < int(n):
                maximo = int(n)

    return maximo


def result():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    fichero = os.path.join(ROOT_DIR, 'words.txt')

    dwords = readdictsword(fichero)
    maximo = max(dwords.keys())
    squares = getdicsquares(maximo)
    # print 'Generación de cuadrados terminada'
    re = 0
    # print dwords

    for k in dwords.keys():
        for w in dwords[k]:
            la = get_anagrames(dwords, w)
            # print w, la
            # ya tenemos lo que es la lista de anagramas, ahora toca buscar un
            # número dentro de los cuadrados que nos sirva
            if len(la) > 0:
                for n in squares[len(w)]:

                    ok, relation = getrelation(w, n)

                    if ok:
                        # print w, n

                        # llegamos aquí, tenemos una letra, un cuadrado
                        # y sabemos que tiene anagramas, pues buscamos en sus
                        # anagramas si vale la relación que tenemos

                        pos = es_posible_resultado(la,
                                                   relation,
                                                   squares[len(w)])
                        if re < pos:
                            re = pos

    # print "Resultado de 0098: ", re
    return re
