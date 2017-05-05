# -*- coding: utf-8 -*-

# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.


# pasados dos enteros, nos dice si tienen los mismos dígitos
def mismosdigitos(n1, n2):
    return bool(''.join(sorted(str(n1))) == ''.join(sorted(str(n2))))


def result():
    n = 1
    while True:

        cumple = True
        for x in 2, 3, 4, 5, 6:
            if not mismosdigitos(n, x * n):
                cumple = False

        if cumple:
            # print("Resultado de 0052:", n)
            # exit(0)
            return n

        n = n + 1
