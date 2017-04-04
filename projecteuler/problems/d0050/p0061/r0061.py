#!/usr/bin/python
# -*- coding: utf-8 -*-


def triangle(n):
    return int(n*(n+1)/2)


def square(n):
    return int(n**2)


def pentagonal(n):
    return int(n*(3*n-1)/2)


def hexagonal(n):
    return int(n*(2*n-1))


def heptagonal(n):
    return int(n*(5*n-3)/2)


def octagonal(n):
    return int(n*(3*n-2))


# joder, le paso la función como parámetro y listo, la uso como fn(n)
def lxnal(fn):
    l = []
    n = 1
    slen = 0
    while slen < 5:
        t = fn(n)
        slen = len(str(t))
        if slen == 4:
            # los que tenga esta forma XX0X no puede entrar ya que obligaria
            # a que el primer digito fuera un 0 y no es posible
            if str(t)[2] != '0':
                l.append(t)
        n += 1
    return l


def cumple(l, solucion):
    laux = list(l)
    solaux = []
    for s in solucion:
        for l in laux:
            if s in l:
                laux.remove(l)
                if s not in solaux:
                    solaux.append(s)

    if len(laux) == 0 and len(solaux) == 6:
        return True
    else:
        return False


def siguientes(e, l):
    sig = []
    for i in l:
        if e % 100 == i / 100:
            sig.append(i)

    return sig


def recursolucion(l, lunida, solucion):

    if len(solucion) == 6:
        if solucion[0] / 100 == solucion[5] % 100:
            if cumple(l, solucion):
                print "Resultado 0061:", solucion, sum(solucion)
        return

    # sacamos el listado de sufijos
    ultimo = solucion[len(solucion)-1]
    sig = siguientes(ultimo, lunida)
    # print "Lista sufijos", ultimo, sig

    for i in sig:
        lunidaaux = list(lunida)
        lunidaaux.remove(i)
        solucionaux = list(solucion)
        solucionaux.append(i)
        # print "Solucion parcial:", lcopysolucion
        recursolucion(l, lunidaaux, solucionaux)


def gensolucion(l, lunida):
    for i in l[0]:
        lunidaaux = list(lunida)
        lunidaaux.remove(i)
        solucion = []
        solucion.append(i)
        recursolucion(l, lunidaaux, solucion)


# variables
l = []

# increiblemente facil
l.append(lxnal(triangle))
l.append(lxnal(square))
l.append(lxnal(pentagonal))
l.append(lxnal(hexagonal))
l.append(lxnal(heptagonal))
l.append(lxnal(octagonal))

lunida = []
for lx in l:
    for i in lx:
        if i not in lunida:
            lunida.append(i)

gensolucion(l, lunida)
