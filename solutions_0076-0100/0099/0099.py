import string

file = open("c:\pedro\euler\base_exp.txt", "r")

# nos quedamos con la primera fila como fila mayor
lvalores = string.split(file.readline(), ',')

base_mayor = float(lvalores[0])
exponente_mayor = float(lvalores[1])
i = 1
i_mayor = 1

#bucle principal
for linea in file:

    i = i + 1

    lvalores = string.split(linea, ',')

    exponente_dividido = float(lvalores[1]) / exponente_mayor

    calculado = float(lvalores[0]) ** exponente_dividido

    if calculado > base_mayor:
        base_mayor = float(lvalores[0])
        exponente_mayor = float(lvalores[1])
        i_mayor = i


print i_mayor