#!/usr/bin/pypy


def is_square(n):
    square = n**0.5
    if int(square) == square:
        return True
    else:
        return False


def diophantine(d, y2):
    x = ((y2*d)+1)**0.5
    if x == int(x):
        return int(x)
    else:
        return -1


D_result = 0
x_min = -1
limite = 1000
for D in range(1, limite+1):
    y = 1
    if not is_square(D):
        dio = False
        while not dio:
            x = diophantine(D, (y*y))
            y += 1
            if x != -1:
                dio = True
                print(D, x)
                if x > x_min:
                    x_min = x
                    D_result = D

print(D_result, x_min)
