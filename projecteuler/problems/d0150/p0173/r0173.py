# -*- coding: utf-8 -*-


def result():

    MAX_TILES = 1000000
    num_solutions = 0

    LIMIT = (MAX_TILES // 8) + 1

    # impares
    for i in range(1, LIMIT):

        tiles = 0
        tiles = (8 * i)

        if tiles <= MAX_TILES:
            num_solutions += 1
        else:
            continue

        for j in range(i + 1, LIMIT):

            new_tiles_to_add = (8 * j)
            tiles += new_tiles_to_add

            if tiles <= MAX_TILES:
                num_solutions += 1
            else:
                break

    # pares
    for i in range(1, LIMIT):

        tiles = 0
        tiles = (8 * i) + 4

        if tiles <= MAX_TILES:
            num_solutions += 1
        else:
            continue

        for j in range(i + 1, LIMIT):

            new_tiles_to_add = (8 * j) + 4
            tiles += new_tiles_to_add

            if tiles <= MAX_TILES:
                num_solutions += 1
            else:
                break

    return num_solutions
