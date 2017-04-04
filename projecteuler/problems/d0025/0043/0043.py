#! /usr/bin/python

import itertools


def property43(n):

    s = str(n)

    if len(s) != 10:
        return False

    if (int(s[1:4])) % 2 != 0:
        return False

    if (int(s[2:5])) % 3 != 0:
        return False

    if (int(s[3:6])) % 5 != 0:
        return False

    if (int(s[4:7])) % 7 != 0:
        return False

    if (int(s[5:8])) % 11 != 0:
        return False

    if (int(s[6:9])) % 13 != 0:
        return False

    if (int(s[7:10])) % 17 != 0:
        return False

    return True

li = []
for i in itertools.permutations('0123456789'):
    x = int("".join(i))
    if (property43(x)):
        li.append(x)

print(sum(li))
