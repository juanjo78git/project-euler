# mymaths algunas funciones que uso mucho

def ispalindrome(n):
    """ Retorna si un numero es palindromo """
    s = str(n)
    for i in range(0, len(s)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True


def isprime(n):
    """ Retorna si un numero es primo """
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



# GENERADORES __________________________________________________________________


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
