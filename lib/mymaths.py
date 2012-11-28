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
