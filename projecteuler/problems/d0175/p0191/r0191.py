# -*- coding: utf-8 -*-


def prize(max_step, step, absent, last_2_days, prizes):
    """ """

    if max_step == step:
        # print(last_2_days)
        # s = ''.join(str(x) for x in last_2_days)
        # s.replace('0', 'O')
        # s.replace('1', 'L')
        # s.replace('2', 'A')
        # print(s)
        return prizes + 1

    # los tres lanzamientos posibles:
    #   - En tiempo: 0
    #   - Tarde: 1
    #   - Falta: 2

    # En tiempo
    prizes = prize(max_step, step + 1, absent, last_2_days[-2:] + [0], prizes)

    # Tarde
    if not absent:
        prizes = prize(max_step, step + 1, True, last_2_days[-2:] + [1],
                       prizes)

    # Falta
    if sum(last_2_days[-2:]) != 4:
        prizes = prize(max_step, step + 1, absent, last_2_days[-2:] + [2],
                       prizes)

    return prizes


def result():
    # print(prize(30, 0, False, [], 0))
    # return prize(4, 0, False, [], 0)
    return prize(30, 0, False, [], 0)
