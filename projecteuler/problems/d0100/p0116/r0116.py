# -*- coding: utf-8 -*-


def tiles(total, offset, size, blocks):
    """ Devuelve los piezas de tamaño *size* que entran en la lista de bloques
        *blocks* a partir del desplazamiento *offset* """

    # Es necesario el offset? SI! para casos como 11011 <-- si no decimos el
    # desplazamiento, jamás podríamos poner el bloque tras el 0

    # 1. Ver si somos capaces de meter otro bloque
    if size > blocks - offset:
        return total

    # 2. Tenemos espacio, pues metemos nuestro bloque a partir del
    # desplazamiento en cadena
    for i in range(offset, blocks):
        # tengo que ver si entra, y lo metemos
        if size <= blocks - i:
            total = tiles(total + 1, i + size, size, blocks)

    return total


def result():

    total = 0

    N_BLOCKS = 50
    TILE_A_SIZE = 2
    TILE_B_SIZE = 3
    TILE_C_SIZE = 4

    total += tiles(0, 0, TILE_A_SIZE, N_BLOCKS)
    total += tiles(0, 0, TILE_B_SIZE, N_BLOCKS)
    total += tiles(0, 0, TILE_C_SIZE, N_BLOCKS)

    return total
