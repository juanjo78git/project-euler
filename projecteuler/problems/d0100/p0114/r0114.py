# -*- coding: utf-8 -*-


def gen_114():
    yield 1
    yield 1
    yield 1
    a = 2
    b = 1
    offset = [1, 1, 0, -1, -1, 0]
    i = 0
    while True:
        yield a
        a, b = a + b + offset[i], a
        i = (i + 1) % len(offset)
        # print('offset', offset[i])


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

    total = 0

    N_BLOCKS = 50
    TILE_MINIM_SIZE = 3

    g = gen_114()
    # total = 0
    # offset = 0
    # tamaño mínimo de azulejos
    # número de bloque
    # que era lo último que le hemos pasado
    for n_b in range(0, N_BLOCKS + 1):
        # recursivo UNICAMENTE para ver como es la secuencia y estudiarla
        # total = tiles_114(0, 0, TILE_MINIM_SIZE, n_b, True, [])
        # print(n_b, total, next(g))
        solucion = next(g)

    return solucion
