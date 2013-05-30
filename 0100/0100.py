#!/usr/bin/python

def first_square(n):
    ''' a partir del n (numero de discos) saco el primer cuadrado posible '''
    while True:
        d = (4 - 8 * (n - (n ** 2)))
        s = d ** 0.5
        if s == int(s):
            return int(s)
        n = n + 1

def get_poss_blue_disk(s):
    ''' determina si el cuadrado es valido, como resultado del num discos'''
    #blue = (2 + float(s)) / float(4)
    blue, m = divmod((2 + s), 4)
    #if int(blue) == blue:
    if m == 0:
        return blue
    else:
        return None

def is_valid_square(s):
    ''' debemos validar que existe un n que cumple lo siguiente
        (4 - 8*(n-n^2)) == s^2. toma!
        
        limpiando un poco... '''

    rd = ((((s * s) - 4) * 32) + 64) ** 0.5
    if int(rd) == rd:
        d, m = divmod((8 + rd), 16)
        #if int(d) == d:
        if m == 0:
            return True, d
        else:
            return False
    else:
        return False

def calc_blue_disk(n):
    fs = first_square(n)
    while True:
        print fs
        valid, n = is_valid_square(fs)
        if valid:
            poss_blue = get_poss_blue_disk(fs)
            if poss_blue != None:
                print 'Resultado encontrado: ', poss_blue, n, fs
                return poss_blue
        fs = fs + 1     

calc_blue_disk(1000000000000)
