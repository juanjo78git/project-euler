# -*- coding: utf-8 -*-
# mymaths algunas funciones que uso mucho


def ispalindrome(n):
    """ Retorna si un numero es palindromo """
    s = str(n)
    for i in range(0, len(s)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True


def isstringpalindrome(s):
    """ Retorna si una cadena es palindromo """
    for i in range(0, len(s)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True


def isprime(n):
    """ Retorna si un numero es primo """
    if n == 0:
        return False

    if n == 1:
        return False

    # rango empieza en 2, y solo tenemos que llegar hasta el cuadrado de n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False

    return True


def ispythagoreantriplet(a, b, c):
    """ Retorna si es una tripleta pitagorica """
    return a**2 + b**2 == c**2


# MUY rapida, eliminamos las demas
def numdivs(n):
    """ Devuelve el total de divisores de un numero """
    # http://mathschallenge.net/library/number/number_of_divisors
    # Basado en:
    # n = p^a * q^b ...
    # d(n) = (a+1)*(b+1)...
    t = 1
    d = 2
    numd = 0            # numero de veces que usamos d
    while n != 1:
        if n % d == 0:
            n = n / d
            numd += 1

            # caso de salida, vaya chapuza, que mal estruturado
            if n == 1:
                t = t * (numd + 1)
        else:
            # si d divide al numero...
            if numd > 0:
                t = t * (numd + 1)

            d += 1
            numd = 0
    return t


def lnumdivs(n):
    """ lista de divisores de un número """
    lidiv = []
    for i in range(1, int((n // 2) + 1)):
        if (n % i == 0):
            lidiv.append(i)
    return lidiv


def numdivsprimes(n):
    """ lista de primos que son divisibles por el numero """
    ldiv = []
    p = prime()
    d = p.__next__()
    while n != 1:
        r, m = divmod(n, d)
        if m == 0:
            n = r
            if d not in ldiv:
                ldiv.append(d)
        else:
            d = p.__next__()

    return ldiv


def factorial(x):
    """ Factorial recursivo """
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


# GENERADORES _________________________________________________________________


def fibonacci():
    """ Generador de la secuencia Fibonacci"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime():
    """ Generador de secuencia numeros primos"""
    p = 2
    while True:
        yield p

        while (not isprime(p + 1)):
            p += 1

        p = p + 1


def trianglenumber():
    """ Generador de secuencia numeros triangulo """
    n = 1
    i = 1
    while True:
        yield n
        n, i = n + i + 1, i + 1


def euler_phi(n):
    """ función phi de euler: número de enteros positivos menores o iguales a n
        y coprimos con n """
    numerador = 1
    denominador = 1
    narg = n

    f = 2
    tratado = False
    while n != 1:
        d, m = divmod(n, f)
        if m == 0:
            if not tratado:
                numerador = (f - 1) * numerador
                denominador = f * denominador
                tratado = True
            n = d
        else:
            f += 1
            tratado = False

    return (narg * numerador) / denominador


# LISTAS ______________________________________________________________________
#

def genlprimes(n):
    """ genera una lista de primos que pueda dividir n """
    l = []
    p = prime()
    myprime = p.__next__()
    # quiero una lista de primos que dividan a n, por lo tanto con
    # buscar solo la mitad me va bien
    limit = n + 1
    while myprime < limit:
        l.append(myprime)
        myprime = p.__next__()

    return l


def genprimes(n1, n2):
    """ genera una lista de primos entre n1 <= prime <= n2 """
    l = []
    p = prime()
    myprime = p.__next__()

    # primero saltamos los que sean menores
    while myprime < n1:
        myprime = p.__next__()

    while myprime <= n2:
        l.append(myprime)
        myprime = p.__next__()

    return l


def factores(n):
    """ factores, pero sin repetir de n """
    lf = []
    f = 2
    inlist = False
    while n != 1:
        d, m = divmod(n, f)
        if m == 0:
            if not inlist:
                lf.append(f)
                inlist = True
            n = d
        else:
            f += 1
            inlist = False

    return lf


# -----------------------------------------------------------------------------

class Fraccion:

    def __init__(self, n, d):
        self.n = n
        self.d = d

    def __mul__(self, other):
        return Fraccion(self.n * other.n, self.d * other.d)

    def __str__(self):
        return '{}/{}'.format(self.n, self.d)

    def simplify(self):
        """ Simplificar la fracción """
        for i in range(2, min(self.n, self.d) + 1):
            exxit = False
            while not exxit:
                if (divmod(self.n, i)[1] == 0) and (divmod(self.d, i)[1] == 0):
                    self.n = self.n // i
                    self.d = self.d // i
                else:
                    exxit = True
