# -*- coding: utf-8 -*-

import math


def discgame(blues, reds, curr_blues, curr_reds, turn, turns, total, visual):
    """ Donde
        blues: discos azules que hay, siempre estará a 1
        reds: discos rojos que hay
        curr_blues: veces que hemos sacado un azul
        turn: turno actual
        turns: turnos a jugar 
        total: tengo que pensármelo """

    den = math.factorial(turns + 1)

    t = 0
    d = 0
    parcial = 0

    if turn == turns:
        if curr_blues > curr_reds:
            print(visual, total)
            return total, den
        else:
            return 0, 0

    # jugamos y sacamos una ficha azul
    t, d = discgame(blues, reds + 1, curr_blues + 1, curr_reds, turn + 1, turns, total, visual + ['A'])
    parcial += t
    
    # jugamos y sacamos una ficha roja
    t, d = discgame(blues, reds + 1, curr_blues, curr_reds + 1, turn + 1, turns, total + reds - 1, visual + ['R'])
    parcial += t

    return parcial, den


def result():
    print('hola')
    
    MAX_TURNS = 5

    total, total2 = discgame(1, 1, 0, 0, 0, MAX_TURNS, 1, [])
    print(total, total2)
    print(divmod(total2, total // 2)[0])

    return 0
