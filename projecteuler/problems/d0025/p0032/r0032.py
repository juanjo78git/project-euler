# -*- coding: utf-8 -*-

# __ PROBLEMA
#
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
# through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.


def pandigital9(m1, m2, r):
    s = str(m1) + str(m2) + str(r)

    if len(s) != 9:
        return False

    # si tiene 0, salimos
    if s.find("0") == 1:
        return False

    for i in range(1, 10):
        if s.find(str(i)) == -1:
            return False
    return True


def ispandigital9(n):
    s = str(n)

    if len(s) != 9:
        return False

    if incluyecero(n):
        return False

    for i in range(1, 10):
        if s.find(str(i)) == -1:
            return False

    return True


def incluyecero(n):
    if str(n).find('0') == -1:
        return False
    else:
        return True


def result():
    lproducts = []
    rango = 99999
    # esto se podría acotar claro, pero como siempre, lo que prima es avanzar y
    # avanzar, por lo que vamos a olvidarnos de hacer que vaya rápido!

    for m1 in range(1, rango):
        for m2 in range(m1, rango):
            product = m1*m2
            pandigital = int(str(m1) + str(m2) + str(product))

            # una vez superado el tamaño 9 break
            if len(str(pandigital)) > 9:
                break

            if ispandigital9(pandigital):
                # solo guardamos el producto que no haya sido ya obtenido
                # independiente del multiplicando o multiplicador
                if product not in lproducts:
                    lproducts.append(product)

    return sum(lproducts)
