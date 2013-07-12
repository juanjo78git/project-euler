#!/usr/bin/python

import os
import sys
lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

import mymaths

f = mymaths.fibonacci()

nf = 0
tf = 0
while len(str(nf)) < 1000:
    nf = f.next()
    tf += 1

# el problema erroneamente considera que el primer termino de la serie
# fibonacci es 1, cuando la realidad es que es 0, por este motivo debo restar
# 1 al valor obtenido por mi bucle
print "Resultado 0025: ", tf - 1
