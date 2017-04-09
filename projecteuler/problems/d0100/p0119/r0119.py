# -*- coding: utf-8 -*-


def sumdigits(n):
    sumatory = 0
    for i in str(n):
        sumatory += int(i)
    return sumatory


def gen_pos_result(N, E):
    powers = []
    for i in range(2, N):
        for j in range(2, E):
            power = i ** j
            if sumdigits(power) == i:
                powers.append(power)
    return powers


def result():
    TH = 30
    # L = 10000
    # N = 10000

    N = 100
    E = 100

    powers = []

    powers = gen_pos_result(N, E)
    powers.sort()

    # print "Resultado de 0123: ", powers[TH - 1]
    result(powers[TH - 1])
