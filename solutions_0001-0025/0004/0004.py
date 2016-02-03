#!/usr/bin/python3

import os
import sys
lib_path = os.path.abspath('../../lib')
sys.path.append(lib_path)

import mymaths

pcapicua = 0
capicua_max = 0

for a in range(100, 1000):
    for b in range(100, 1000):
        pcapicua = a * b

        if mymaths.ispalindrome(pcapicua):
            if capicua_max < pcapicua:
                capicua_max = pcapicua

print ("Resultado 0004: ", capicua_max)
