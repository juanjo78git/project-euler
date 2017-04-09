# -*- coding: utf-8 -*-

from projecteuler import mymaths


def gen_list_square(limit):
    """ lista de cuadrados hasta un límite """
    l = []
    for i in range(1, limit):
        square = i*i
        if square > limit:
            break
        else:
            l.append(square)

    return l


def gen_list_palindromic(limit):
    """ lista de palíndromos hasta un límite """
    l = []
    for i in range(1, limit + 1):
        if mymaths.ispalindrome(i):
            l.append(i)

    return l


def is_0125(squares, p):
    """ dado una lista de cuadrados y un palindromo intenta ver si cumple """
    for i in range(len(squares)):
        # si el cuadrado ya es mayor que p debemos salir
        if squares[i] > p:
            break
        for j in range(i + 2, len(squares)):
            sumatory = sum(squares[i:j])
            if sumatory == p:
                return True
            elif sumatory > p:
                break

    return False


def result():
    LIMITE = 100000000
    # LIMITE = 1000

    squares = gen_list_square(LIMITE)
    palindromic = gen_list_palindromic(LIMITE)

    # print "Total palíndromos: %d" % len(palindromic)
    # print "Total cuadrados: %d" % len(squares)

    total = 0
    for p in palindromic:
        if is_0125(squares, p):
            total += p

    # print "Resultado de 0125 ", total
    return total
