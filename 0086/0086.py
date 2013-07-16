# -*- coding: utf-8 -*-

#!/usr/bin/python

import os
import sys
from datetime import datetime

lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

import mymaths

LIMITE = 1000000

calculados = []
cadena_maxima = []

# controlamor el tiempo de ejecución
start_time = datetime.now()

for n in range(4, LIMITE):

    if n % 1000 == 0:
        print n

    # primero vemos que no lo hemos estudiado ya
    #if n in calculados:
        #continue
    #else:
        #calculados.append(n)
    cadena = [n]

    nex = n
    while True:
        #print n
        # generamos el siguiente:

        nex = sum(mymaths.lnumdivs(nex))
        #calculados.append(nex)

        # condiciones de salida
        if nex == n:
            if len(cadena_maxima) < len(cadena):
                print cadena_maxima
                print cadena
                cadena_maxima = cadena
            break

        if nex > LIMITE:
            break

        # controlamos un ciclo para salir
        if nex in cadena:
            break

        cadena.append(nex)
        #print n, cadena


print cadena_maxima
print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0095: ", cadena_maxima[0]
