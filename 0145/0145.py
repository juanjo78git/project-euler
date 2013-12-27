# -*- coding: utf-8 -*-

#!/usr/bin/python

# Algunos enteros positivos n tienen la propiedad de que la suma
# [ n + invertido(n) ] se compone enteramente de dígitos impares (decimales).
# Por ejemplo, 36 + 63 = 99 y 409 + 904 = 1313. Vamos a llamar a estos números
# reversibles; de modo que 36, 63, 409, y 904 son reversibles. No se permiten
# ceros a la izquierda en n ni en invertido(n).
#
# Hay 120 números reversibles por debajo de mil.
#
# ¿Cuántos números reversibles hay por debajo de mil millones (10^9)?


from datetime import datetime


def is_reversible(n):
    # si termina por cero no lo queremos, por restricciones del problema
    if n % 10 == 0:
        return False
    # invertimos el número
    ni = int(str(n)[::-1])
    nr = ni + n
    for c in str(nr):
        if int(c) % 2 == 0:
            return False
    return True


start_time = datetime.now()

LIMITE = 1000000000
# LIMITE = 100000
total = 0

for n in range(1, LIMITE):

    if n % 1000000 == 0:
        print n, total

    if is_reversible(n):
        total += 1

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0145: ", total
