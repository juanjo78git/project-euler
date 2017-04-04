#!/usr/bin/python


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


number = 1
maxpandigital = -1

while (number < 1000000):

    n = 1
    concatnumber = ""
    while (True):
        prod = n * number
        if incluyecero(prod):
            break

        concatnumber = concatnumber + str(prod)

        if (len(concatnumber) > 9):
            break

        if ispandigital9(int(concatnumber)):
            if (maxpandigital < int(concatnumber)):
                maxpandigital = int(concatnumber)
            break

        n = n + 1

    number = number + 1

print "Máximo pandigital: ", maxpandigital
