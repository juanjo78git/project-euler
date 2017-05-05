# -*- coding: utf-8 -*-


def tiles_114(total, offset, min_size, total_blocks, was_last_space, solution):

    if offset == total_blocks:
        # Es solucion
        # print(solution)
        return total + 1

    if offset > total_blocks:
        # no es solución
        return total

    # podemos intentar meter un espacio
    total = tiles_114(total, offset + 1, min_size, total_blocks, True,
                      solution + ['S'])

    # Si lo ultimo fue un espacio, podemos meter fichas
    if was_last_space:
        for tile_size in range(min_size, total_blocks + 1):

            # intentamos meter tiles de tamaño size
            total = tiles_114(total, offset + tile_size, min_size,
                              total_blocks, False, solution + [tile_size])

    return total


def result():

    # TILE_MINIM_SIZE = 3
    # TOTAL_NUMBERS_BLOCKS = 30
    # total = tiles_114(0, 0, 3, 29, True, [])
    # total = tiles_114(0, 0, 10, 56, True, [])
    num_blocks = 0
    total = 0
    while total < 1000000:
        total = tiles_114(0, 0, 50, num_blocks, True, [])
        # print(num_blocks, total)
        num_blocks += 1

    return num_blocks
