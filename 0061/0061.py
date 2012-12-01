#!/usr/bin/python
# -*- coding: utf-8 -*-


# idea para limpiar
#
# no lo metas en una lista general, ve sacando los datos de las
# listas individuales y luego vas viendo que listas has usado
# y cuales no. joder, como el del foro... o intenta dejar esta 
# solución lo más simple posible

import itertools

def triangle(n):
    return int(n*(n+1)/2)

def square(n):
    return int(n**2)

def pentagonal(n):
    return int(n*(3*n-1)/2)

def hexagonal(n):
    return int(n*(2*n-1))

def heptagonal(n):
    return int(n*(5*n-3)/2)

def octagonal(n):
    return int(n*(3*n-2))

# joder, le paso la función como parámetro y listo, la uso como fn(n)
def lxnal(fn):
    l = []
    n = 1
    mini = 99999
    maxi = 0
    slen = 0
    while slen < 5:
        t = fn(n)
        slen = len(str(t))
        if slen == 4:
            # los que tenga esta forma XX0X no puede entrar ya que obligaria
            # a que el primer digito fuera un 0 y no es posible
            if str(t)[2] != '0':
                l.append(t)
        n += 1
    return l


def esciclico_quick(l, ndc):
    ''' Retorna si una lista es ciclica en ndc factores por digito, pero esta
    vez muy rapida, el metodo anterior era un puto desastre '''
    lpre = []
    lsuf = []

    for li in l:
        lpre.append(str(li)[ndc:])
        lsuf.append(str(li)[0:ndc])

    lpre.sort()
    lsuf.sort()
    if set(lpre) == set(lsuf):
        # puede haber falsos positivos
        return esciclico_ordenado(l, ndc)
    else:
        return False

def esciclico(l, ndc):
    ''' Retorna si es ciclico, a partir de un listado
    l: listado, ndc: numero de digitos ciclicos '''
    n = len(l)

    for i in range(0, n):
        j = i
        k = (i + 1) % n
        # final con inicio
        if str(l[j])[ndc:] != str(l[k])[0:ndc]:
            return False
    return True


def esciclico_ordenado(l, ndc):
    ''' A partir de un listado, nos dice si es ciclico cualquiera de las
    permutaciones pusibles '''
    for lp in itertools.permutations(l):
        if esciclico(lp, ndc):
            return True

    return False



def lsufijos(elemento, l):
    lsuf = []
    for i in l:
        if str(elemento)[2:] == str(i)[0:2]:
            lsuf.append(i)

    return lsuf


def edl(lista, lsolucion):
    for i in lsolucion:
        if i in lista:
            return True

    return False

def estadiflistas(ltotal, lsolucion):
    for li in ltotal:
        if not edl(li, lsolucion):
            return False

    return True
        



def ryp(ltotal, l, lsolucion):

    if len(lsolucion) == 6:
        if esciclico_quick(lsolucion, 2):
            if estadiflistas(ltotal, lsolucion):
                lsolucion.sort()
                print "Solucion Final:", lsolucion, sum(lsolucion)
        return

    # sacamos el listado de sufijos
    ultimo = lsolucion[len(lsolucion)-1]
    lsuf = lsufijos(ultimo, l)
    #print "Lista sufijos", ultimo, lsuf

    for i in lsuf:
        lcopy = list(l)
        lcopy.remove(i)
        lcopysolucion = list(lsolucion)
        lcopysolucion.append(i)
        #print "Solucion parcial:", lcopysolucion
        ryp(ltotal, lcopy, lcopysolucion)

    



# variables
numero_digitos_ciclicos = 2
np = 6
l = []

# increiblemente facil
l.append(lxnal(triangle))
l.append(lxnal(square))
l.append(lxnal(pentagonal))
l.append(lxnal(hexagonal))
l.append(lxnal(heptagonal))
l.append(lxnal(octagonal))

ltotal = []
for lx in l:
    for i in lx:
        if i not in ltotal:
            ltotal.append(i)

ltotal.sort()

for i in ltotal:
    laux = list(ltotal)
    laux.remove(i)
    lsol = []
    lsol.append(i)
    ryp(l, laux, lsol)



count = 0
total = 0
# vamos a ver, voy a intentar ejecutar esto...

#for i in range(0, 6):
    #print len(l[i])



#for n3 in l[0]:
    #for n4 in l[1]:
        #for n5 in l[2]:
            #for n6 in l[3]:
                #for n7 in l[4]:
                    #for n8 in l[5]:
                        #laux = []
                        #laux.append(n3)
                        #laux.append(n4)
                        #laux.append(n5)
                        #laux.append(n6)
                        #laux.append(n7)
                        #laux.append(n8)
                        #count += 1
                        #total += 1
                        #if count == 1000000:
                            #count = 0
                            #print total

                        #if esciclico_quick(laux, 2):
                            #print("Resultado provisional:", laux)
                            #lresult = list(laux)


#print("Resultado 0061:", sum(lresult))



#li = 0
#lcopy = list(l)
#print(id(lcopy), id(l))
#for lx in l:
    #lminus = list(l)
    #lminus.pop(li)
    #for i in lx:
        #if not busca_pre_suf(i, lminus):
            #lcopy[li].remove(i)

    #li += 1


#for lx in lcopy:
    #print(len(lx))
    ##print(lx)

