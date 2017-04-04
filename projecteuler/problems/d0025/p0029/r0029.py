# -*- coding: utf-8 -*-

#!/usr/bin/python

import os
import sys
from datetime import datetime

lib_path = os.path.abspath('../../lib')
sys.path.append(lib_path)

# controlamor el tiempo de ejecución
start_time = datetime.now()

l = []

for a in range(2, 101):
    for b in range(2, 101):
        if a ** b not in l:
            l.append(a ** b)

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0028:", len(l)
