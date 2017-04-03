# -*- coding: utf-8 -*-

import os
import sys

from projecteuler import mymaths

def result():
    # el iterador
    p = mymaths.prime()

    limite = 10001

    for i in range(1, limite):
        p.__next__()

    return p.__next__()
