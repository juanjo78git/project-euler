#!/usr/bin/python

import os
import sys
lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

import mymaths

# el iterador
p = mymaths.prime()

limite = 10001

for i in range(1, limite):
    p.next()

# el resultado estara en el siguiente
print "Resultado 0007: ", p.next()
