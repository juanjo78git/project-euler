# -*- coding: utf-8 -*-

#!/usr/bin/python

import os
import sys
import itertools
from datetime import datetime

lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

# controlamor el tiempo de ejecución
start_time = datetime.now()

# el generador...
g = itertools.permutations(range(0, 10))

c = 0
while c != 1000000:
    result = g.next()
    c += 1

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0024:", ''.join([str(x) for x in result])
