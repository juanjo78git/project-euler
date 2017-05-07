# -*- coding: utf-8 -*-


def fibonacci_minus_1():
    """ Generador de la secuencia Fibonacci"""
    a, b = 1, 1
    while True:
        if a == 0:
            yield 0
        else:
            yield a - 1
        a, b = b, a + b


def tiles_size_3():
    """ El peor generador de la historia, o al menos muy guarro """
    n = 0
    n_1 = 1
    n_2 = 0
    n_ant_1 = 0
    n_ant_2 = 0
    n_ant_3 = 0
    n_ant_4 = 0
    n_ant_5 = 0
    yield 0
    yield 0
    yield 0
    while True:
        n_2 = n + n_1 - n_ant_5
        # print('X', n_2, n, n_1, n_ant_5)
        yield n_2
        n = n_1
        n_1 = n_2
        n_ant_5 = n_ant_4
        n_ant_4 = n_ant_3
        n_ant_3 = n_ant_2
        n_ant_2 = n_ant_1
        n_ant_1 = n_2


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
    # TILE_A_SIZE = 2
    # TILE_B_SIZE = 3
    TILE_C_SIZE = 4

    g_a = fibonacci_minus_1()
    g_b = tiles_size_3()

    for _ in range(0, N_BLOCKS):
        next(g_a)
        next(g_b)

    # Ahora lo hago por secuencia, pero para C no la he conseguido
    total = next(g_a)
    # total += tiles(0, 0, TILE_A_SIZE, N_BLOCKS)
    total += next(g_b)
    # total += tiles(0, 0, TILE_B_SIZE, N_BLOCKS)

    total += tiles(0, 0, TILE_C_SIZE, N_BLOCKS)

    return total
