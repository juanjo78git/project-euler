# -*- coding: utf-8 -*-


from projecteuler import mymaths

def result():
    f = mymaths.fibonacci()

    nf = 0
    tf = 0
    while len(str(nf)) < 1000:
        nf = f.__next__()
        tf += 1

    # el problema erroneamente considera que el primer termino de la serie
    # fibonacci es 1, cuando la realidad es que es 0, por este motivo debo
    # restar 1 al valor obtenido por mi bucle
    return (tf - 1)
