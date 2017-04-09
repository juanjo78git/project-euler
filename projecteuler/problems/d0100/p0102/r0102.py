# -*- coding: utf-8 -*-

import os


class Punto:
    """ Un punto """
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


class Triangulo:
    """ Un triángulo """
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def orientacion(self):
        """ obtenemos la orientación de un triángulo """
        if (((self.p1.x - self.p3.x) * (self.p2.y - self.p3.y)) -
                ((self.p1.y - self.p3.y) * (self.p2.x - self.p3.x))) < 0:
            return False
        else:
            return True

    def punto_en_triangulo(self, po):
        """ a partir del triángulo y de un punto origen """
        or_0 = self.orientacion()
        t1 = Triangulo(self.p1, self.p2, po)
        or_1 = t1.orientacion()
        t2 = Triangulo(self.p2, self.p3, po)
        or_2 = t2.orientacion()
        t3 = Triangulo(self.p3, self.p1, po)
        or_3 = t3.orientacion()
        if or_0 == or_1 and or_1 == or_2 and or_2 == or_3:
            return True
        else:
            return False


def result():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    fichero = os.path.join(ROOT_DIR, 'triangles.txt')

    f = open(fichero)

    inside = 0
    po = Punto(0, 0)

    for l in f:
        lp = l.replace('\n', '').split(',')
        p1 = Punto(lp[0], lp[1])
        p2 = Punto(lp[2], lp[3])
        p3 = Punto(lp[4], lp[5])

        t = Triangulo(p1, p2, p3)

        if t.punto_en_triangulo(po):
            inside += 1

    # print "Resultado 0102: ", inside
    return inside
