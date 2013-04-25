def p100(n):
    salida = False
    nf = float(n)
    while salida == False:
        d = 4 - 8*(nf - (nf ** 2))
        rd = float(d) ** 0.5
        if int(rd) == rd:
            r = (2 + float(rd))/float(4)
            if int(r) == r:
                print "Resultado: ", int(r), int(n)
                salida = True
        n = n + 1
        if n % 10000000 == 0:
            print n




# por partes
#
# 1. una función que me diga el primer cuadrado que cumple


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
    blue = (2 + float(s)) / float(4)
    if int(blue) == blue:
        return int(blue)
    else:
        return None

def is_valid_square(s):
    ''' debemos validar que existe un n que cumple lo siguiente
        (4 - 8*(n-n^2)) == s^2. toma!
        
        limpiando un poco... '''

    rd = ((((s * s) - 4) * 32) + 64) ** 0.5
    if int(rd) == rd:
        d = (8 + rd)/float(16)
        if int(d) == d:
            return True
        else:
            return False
    else:
        return False

def calc_blue_disk(n):
    fs = first_square(n)
    while True:
        print fs
        if is_valid_square(fs):
            poss_blue = get_poss_blue_disk(fs)
            if poss_blue != None:
                print 'Resultado encontrado: ', poss_blue
                return poss_blue
        fs = fs + 1     
