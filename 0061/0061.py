#!/usr/bin/python
# -*- coding: utf-8 -*-

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


def limpiar_listas(l):

    # prefijo serían ya los dos dos primeros números
    def tiene_prefijo(pre, l):
        for x in l:
            if pre == str(x)[0:2]:
                return True
        return False

    def tiene_sufijo(suf, l):
        for i in l:
            if suf == str(i)[2:4]:
                return True
        return False

    def busca_pre_suf(n, l):
        #print(n, i, l)

        pre = str(n)[0:2]
        suf = str(n)[2:4]
        bpre = False
        bsuf = False

        for lx in l:
            if tiene_prefijo(pre, lx):
                bpre = True

            if tiene_sufijo(suf, lx):
                bsuf = True

        return bpre and bsuf


    li = 0
    lcopy = list(l)
    print(id(lcopy), id(l))
    for lx in l:
        lminus = list(l)
        lminus.pop(li)
        for i in lx:
            if not busca_pre_suf(i, lminus):
                lcopy[li].remove(i)

        li += 1






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

# intentamos limpiar... con un poco de suerte
#
#for i in 

limpiar_listas(l)

for lx in l:
    print(len(lx))
    #print(lx)











count = 0
total = 0
# vamos a ver, voy a intentar ejecutar esto...

#for i in range(0, 6):
    #print len(l[i])



for n3 in l[0]:
    for n4 in l[1]:
        for n5 in l[2]:
            for n6 in l[3]:
                for n7 in l[4]:
                    for n8 in l[5]:
                        laux = []
                        laux.append(n3)
                        laux.append(n4)
                        laux.append(n5)
                        laux.append(n6)
                        laux.append(n7)
                        laux.append(n8)
                        count += 1
                        total += 1
                        if count == 1000000:
                            count = 0
                            print total

                        if esciclico_quick(laux, 2):
                            print("Resultado provisional:", laux)
                            lresult = list(laux)


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

