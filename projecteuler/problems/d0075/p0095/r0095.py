# -*- coding: utf-8 -*-

import os
import sys

from projecteuler import mymaths

def result():
    LIMITE = 1000000

    calculados = []
    cadena_maxima = []

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

    # print cadena_maxima
    return int(cadena_maxima[0])
