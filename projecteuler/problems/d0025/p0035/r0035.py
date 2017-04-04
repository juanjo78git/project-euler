# -*- coding: utf-8 -*-


def isprime(n):
    if n == 1:
        return False

    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def rotateprime(n):

    s = str(n)

    while True:

        s = s[1:]+s[0]

        if (s == str(n)):
            return True

        if not isprime(int(s)):
            return False


def result():
    n = 1
    total = 0
    while (n < 1000000):

        if (isprime(n)):

            if (rotateprime(n)):
                total = total + 1

        n = n + 1

    return total
