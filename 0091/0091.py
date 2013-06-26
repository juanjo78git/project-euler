# -*- coding: utf-8 -*-

#!/usr/bin/python

from datetime import datetime


class Punto:
    """ Punto en coordenadas """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return ((self.x == other.x) and (self.y == other.y))

    def is_rigth_triangle(self, q, r):
        """ tengo que ver si es un triangulo rectángulo """

        pq = ((self.x - q.x) ** 2) + ((self.y - q.y) ** 2)
        pr = ((self.x - r.x) ** 2) + ((self.y - r.y) ** 2)
        qr = ((q.x - r.x) ** 2) + ((q.y - r.y) ** 2)

        # vemos cual es el mayor
        if pq > pr:
            if pq > qr:
                hipo = pq
                cat1 = qr
                cat2 = pr
            else:
                hipo = qr
                cat1 = pq
                cat2 = pr
        else:
            if pr > qr:
                hipo = pr
                cat1 = qr
                cat2 = pq
            else:
                hipo = qr
                cat1 = pq
                cat2 = pr

        return (hipo == cat1 + cat2)

LIMITE = 50

# controlamor el tiempo de ejecución
start_time = datetime.now()

raiz = Punto(0, 0)
total = 0

# Aparecen dos veces el mismo triángulo, en fin, me da igual luego divido
# por dos, no tengo ganas de ir viendo si unos puntos u otros están dos veces
for x1 in range(0, LIMITE + 1):
    for y1 in range(0, LIMITE + 1):
        for x2 in range(0, LIMITE + 1):
            for y2 in range(0, LIMITE + 1):

                # no tengo ganas de pensar mucho...
                p1 = Punto(x1, y1)
                p2 = Punto(x2, y2)

                if raiz == p1 or raiz == p2:
                    continue

                if p1 == p2:
                    continue

                if raiz.is_rigth_triangle(p1, p2):
                    total += 1

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0091: ", total / 2
