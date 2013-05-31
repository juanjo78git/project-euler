# -*- coding: utf-8 -*-

#!/usr/bin/pypy

import os
import sys
from datetime import datetime

lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

import mymaths

# controlamos el tiempo de ejecución
start_time = datetime.now()

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0075: "
