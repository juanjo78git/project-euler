# -*- coding: utf-8 -*-

#!/usr/bin/python

import os
import sys
from datetime import datetime

lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

# controlamor el tiempo de ejecución
start_time = datetime.now()

t = 1
n = 1
for s in range(2, 1001, 2):
    for i in range(0, 4):
        n = n + s
        t += n

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0028:", t
