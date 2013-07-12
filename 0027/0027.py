#!/usr/bin/python2


def isprime(n):
    if n <= 1:
        return False

    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def cuadratic_prime(n, a, b):
    return isprime(n**2 + a*n + b)


amax = None
bmax = None
nmax = None
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        n = 0
        while (cuadratic_prime(n, a, b)):
            n = n + 1

        if (n > nmax):
            nmax = n
            amax = a
            bmax = b

print amax*bmax
