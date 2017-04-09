# -*- coding: utf-8 -*-

import math


def is_0206(n):
    s = str(n)
    if len(s) == 19:
        return (s[0] == '1' and s[2] == '2' and s[4] == '3' and s[6] == '4'
                and s[8] == '5' and s[10] == '6' and s[12] == '7' and
                s[14] == '8' and s[16] == '9' and s[18] == '0')
    else:
        return False


def result():

    maximo = int(math.sqrt(1929394959697989990)) + 1
    minimo = int(math.sqrt(1020304050607080900)) - 1

    for n in range(minimo, maximo):
        # if n % 1000000 == 0:
        #     print n
        square = n * n
        if is_0206(square):
            break

    # print(square, n)
    return n
