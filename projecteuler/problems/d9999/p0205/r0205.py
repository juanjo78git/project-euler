# -*- coding: utf-8 -*-

import itertools


def count_perm(l, size):
    return len(list(set((itertools.permutations(l, size)))))


def prob_pyram_cubic(pyramidal_dice, cubic_dice):

    cs = list(itertools.combinations_with_replacement([1, 2, 3, 4, 5, 6],
                                                      cubic_dice))
    ps = list(itertools.combinations_with_replacement([1, 2, 3, 4],
                                                      pyramidal_dice))

    win_p = 0
    t_p = 1
    t_c = 1
    now = False

    for p in ps:
        now = True
        for c in cs:
            if sum(p) > sum(c):
                # LLLLLLLLLLLLLLLLLLegados a este punto, queremos saber cuantas
                # de esas combinaciones se pueden dar, y para eso usamos
                # permutaciones
                if now:
                    t_p = count_perm(p, pyramidal_dice)
                now = False
                t_c = count_perm(c, cubic_dice)

                win_p += ((1 / (6 ** cubic_dice)) *
                          (1 / (4 ** pyramidal_dice))) * t_p * t_c

    return win_p


def result():
    num_pyramidal_dice = 9
    num_cubic_dice = 6
    p = prob_pyram_cubic(num_pyramidal_dice, num_cubic_dice)

    # retornamos el valor como 0.abcdefg
    return '%.7f' % p
