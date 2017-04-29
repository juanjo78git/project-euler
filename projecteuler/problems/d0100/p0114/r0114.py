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

    total = 0

    N_BLOCKS = 50
    # N_BLOCKS = 7
    TILE_MINIM_SIZE = 3
    
    # total = 0
    # offset = 0
    # tamaño mínimo de azulejos
    # número de bloque
    # que era lo último que le hemos pasado
    for n_b in range(0, N_BLOCKS + 1):
        total = tiles_114(0, 0, TILE_MINIM_SIZE, n_b, True, [])
        print(n_b, total)

    return total
