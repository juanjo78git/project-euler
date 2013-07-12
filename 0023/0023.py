#!/usr/bin/python2


def p23():

    def es_abundante(n):
        divisores = []
        for i in range(1, n/2 + 1):
            if not (n % i):
                divisores.append(i)
        return sum(divisores) > n

    def lista_abundantes():
        abundantes = []
        for i in range(1, 28123 + 1):
            if (es_abundante(i)):
                abundantes.append(i)
        return abundantes

    abundantes = []
    abundantes = lista_abundantes()

    print abundantes

    #for i in abundantes:
    #    print i

    # vamos a buscar n != a1 + a2

    no_suma_abundantes = []
    for n in range(1, 28123 + 1):

        es_suma_abundantes = False
        a2 = 0

        for a1 in abundantes:
            if (n < a1):
                break

            a2 = n - a1
            if (a2 in abundantes):
                es_suma_abundantes = True
                break

        # si es True no se muestra
        if not es_suma_abundantes:
            print "resultado: " + str(n) + "=" + str(a1) + "+" + str(a2)
            no_suma_abundantes.append(n)

    #print no_suma_abundantes
    print sum(no_suma_abundantes)


p23()
