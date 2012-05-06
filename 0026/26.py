def lista_restos(dividendo, divisor):

    lista = []

    while (True):

        while (dividendo < divisor):
            dividendo = dividendo * 10

        resto = dividendo % divisor
        dividendo = dividendo % divisor

        if resto == 0:
            break

        # si el resto no es 0, vemos si esta ya el resto en
        # la lista

        if resto in lista:
            break
        else:
            lista.append(resto)

    # vemos el motivo por el que hemos salido
    print lista
    if resto != 0:
        return len(lista) - lista.index(resto)

maxi = 0
number = 0
for d in range(2, 1001):
    i = lista_restos(1, d)
    if i > maxi:
        maxi = i
        number = d

print maxi
print number

