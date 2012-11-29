#!/usr/bin/python

import os, sys
lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

import mymaths

f100 = mymaths.factorial(100)
suma = 0

for i in range(0, len(str(f100))):
    suma += int(str(f100)[i])


print ("Resultado 0020", suma)
