# -*- coding: utf-8 -*-

import os
import sys

from projecteuler import mymaths

def result():
    pcapicua = 0
    capicua_max = 0

    for a in range(100, 1000):
        for b in range(100, 1000):
            pcapicua = a * b

            if mymaths.ispalindrome(pcapicua):
                if capicua_max < pcapicua:
                    capicua_max = pcapicua

    return capicua_max
