#!/usr/bin/python

import os
import sys
lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

import mymaths

# numero de divisores minimo que buscamos
nmindivs = 500

t = mymaths.trianglenumber()

while True:
    n = t.next()
    if mymaths.numdivs(n) > nmindivs:
        break

print "Resultado 0012: ", n
