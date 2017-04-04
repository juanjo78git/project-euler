# -*- coding: utf-8 -*-

# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.
#
# 9 = 7 + 212
# 15 = 7 + 222
# 21 = 3 + 232
# 25 = 7 + 232
# 27 = 19 + 222
# 33 = 31 + 212
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of
# a prime and twice a square?

# idea:
#
# listade primos = dame lista de primos
#
# for n in range(impares):
#    if n es primo:
#        break
#
#    buscamos en nuestra lista de primos el primer elemento i mayor que n
#    for (0 to elemento i que sabemos que es el primo mayor que n):
#        for j in range(1 .. raizcuadrada(n/2) +1
#
#            if (n == listadeprimos[i] + 2*j^2):
#                print(n)
#                exit(0)
# solucionado! a falta de picar (eso espero!)
# los tiempos serán buenos... el único problema es delimitar cuandos primos
# guardamos, aunque una chapuza sería para cada bucle generar un listado
# de primos menos que n... me-nu-da chapuza... --> quizás mejor sería que
# el bucle del medio estuviera el último, que es el más pesado por el tema
# de los primos... <-- gran idea#! /usr/bin/python


def isprime(n):
    if n == 1:
        return False

    # rango empieza en 2, y solo tenemos que llegar hasta el cuadrado de n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def lista_n_primos(n):
    """ un listado de n números primos """
    lprimos = []
    j = 2

    while len(lprimos) != n:
        if isprime(j):
            lprimos.append(j)
            # if (len(lprimos) % 1000) == 0:
            #     print("Procesados", len(lprimos), "primos de un total de", n)
        j = j + 1

    return lprimos


def pos_primo_mayor(l, n):
    """ retorna el indice del siguiente elemento mayor que n, la lista debe
        estar ordenada! """
    for i in range(0, len(l)):
        if l[i] > n:
            return i


# main
# 9 = 7 + 2*1^2
# impar = primo + 2    * n^2


def result():
    lprimos = lista_n_primos(100000)

    # print("Lista de 100000 generada")

    # primer impar no primo!
    impar = 9
    goldbach = False

    while True:
        if not isprime(impar):

            # esto se podría mejorar con el rango de abajo...
            rango_primo = pos_primo_mayor(lprimos, impar)
            for n in range(1, int(((impar/2)**0.5)+1)):
                for iprimo in range(0, rango_primo):
                    goldbach = False

                    # y ahroa el cálculo entero
                    if (impar == lprimos[iprimo] + (2*(n**2))):
                        # print("Es Goldbach:", impar, "=", lprimos[iprimo],
                        #     "+ 2 x ", n, "^2")
                        goldbach = True
                        break

                # al terminar el bucle comprobamos si existía una combinación
                # correcta
                if goldbach:
                    break

            if not goldbach:
                print("No cumple Goldbach el impar", impar)
                # exit(0)
                continue

        impar = impar + 2
        # if (impar % 1001) == 0:
            # print("Tratamiento del impar:", impar)

    # print(lprimos)

    i = pos_primo_mayor(lprimos, 55)

    print(lprimos[i], lprimos[i-1])
    return lprimos[i]

