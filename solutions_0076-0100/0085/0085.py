# -*- coding: utf-8 -*-

#!/usr/bin/pypy

from datetime import datetime

CUADRADOS = 2000000


def calc_cuadraditos(x, y):
    t = 0
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            t += i * j
    return t


start_time = datetime.now()

near = 0
x_res = 0
y_res = 0
for x in range(1, 100):
    for y in range(1, 100):
        nc = calc_cuadraditos(x, y)
        if nc > CUADRADOS:
            break

        if nc > near:
            near = nc
            x_res = x
            y_res = y

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0085: ", x_res * y_res
