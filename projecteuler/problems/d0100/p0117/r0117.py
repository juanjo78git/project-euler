# -*- coding: utf-8 -*-


def tiles(total, offset, sizes, blocks):
    """ Devuelve los piezas de tamaño *size* que entran en la lista de bloques
        *blocks* a partir del desplazamiento *offset* """

    # Es necesario el offset? SI! para casos como 11011 <-- si no decimos el
    # desplazamiento, jamás podríamos poner el bloque tras el 0

    # 1. Ver si somos capaces de meter otro bloque
    # if size > blocks - offset:
    #     return total

    # 2. Tenemos espacio, pues metemos nuestro bloque a partir del
    # desplazamiento en cadena
    for i in range(offset, blocks):
        for size in sizes:
            # tengo que ver si entra, y lo metemos
            if size <= blocks - i:
                total = tiles(total + 1, i + size, sizes, blocks)
            # else:
            #     continue

    return total



def tetranacci():
    """ Tetranacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4)
        with a(0)=a(1)=a(2)=0, a(3)=1. 
        (Formerly M1108 N0423)
        https://oeis.org/A000078 """

    a_0 = 0
    a_1 = 0
    a_2 = 0
    a_3 = 1
    while True:
        a_n = a_0 + a_1 + a_2 + a_3
        yield a_n
        a_4 = a_3
        a_3 = a_2
        a_2 = a_1
        a_1 = a_0
        a_0 = a_n


def result():

    total = 0

    N_BLOCKS = 50
    TILE_A_SIZE = 2
    TILE_B_SIZE = 3
    TILE_C_SIZE = 4

    # La solución recursiva no termina
    # total = tiles(0, 0, [TILE_A_SIZE, TILE_B_SIZE, TILE_C_SIZE], N_BLOCKS)

    t = tetranacci()

    for i in range(0, N_BLOCKS + 1):
        solucion = next(t)
        # print(i, solucion)

    # falta incluir la que no tiene NINGÚNA tile
    # total += 1

    return solucion
