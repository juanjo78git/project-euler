# -*- coding: utf-8 -*-


def isprime(n):
    if n == 1 or n == 0:
        return False
    # rango empieza en 2, y solo tenemos que llegar hasta el cuadrado de n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def nextprime(n):
    while not isprime(n+1):
        n = n + 1
    return n + 1


def lprimepower(limit):

    p = 2
    lprimes2 = []
    lprimes3 = []
    lprimes4 = []
    exxit = False

    while not exxit:
        if p**2 < limit:
            lprimes2.append(p**2)
        else:
            exxit = True

        if p**3 < limit:
            lprimes3.append(p**3)

        if p**4 < limit:
            lprimes4.append(p**4)

        p = nextprime(p)

    return lprimes2, lprimes3, lprimes4


def result():
    limit = 50000000
    l2, l3, l4 = lprimepower(limit)

    # print(len(l2))
    # print(len(l3))
    # print(len(l4))

    ltotal = []
    count = 0
    for i2 in l2:
        count += 1
        # if count % 10 == 0:
        #     print(count)
        for i3 in l3:
            if i2+i3 > limit:
                break
            for i4 in l4:
                zum = i2+i3+i4
                if zum < limit:
                    if zum not in ltotal:
                        ltotal.append(zum)
                else:
                    break

    # print('Resultado 0087:', len(ltotal))
    return len(ltotal)
