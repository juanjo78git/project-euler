# -*- coding: utf-8 -*-


def pentagonal(n):
    """ el termino n es dado por (3n^2-n)/2 """
    return ((n * (3 * n - 1)) // 2)


def generalised_pentagonal(n):
    """ dependiendo de si es par o impar """
    if n % 2 == 0:
        return pentagonal((n // 2) + 1)
    else:
        return pentagonal(-(n // 2) - 1)


def termsign(i):
    if i % 4 < 2:
        # add if i mod 4 is 0 or 1
        return 1
    else:
        # subtract otherwise
        return -1


def result():
    DIVISOR = 1000000

    pt = [1]
    n = 0
    while True:
        n += 1
        r = 0
        i = 0
        while True:
            k = generalised_pentagonal(i)
            if k > n:
                break
            # print(n - k)
            r += termsign(i) * pt[int(n - k)]
            i += 1
        pt.append(r)
        if r % DIVISOR == 0:
            break

    # print "Resultado de 0078: ", n
    return n


if __name__ == '__main__':
    result()
