# -*- coding: utf-8 -*-

#!/usr/bin/python

from datetime import datetime


LIMITE = 1000

# controlamor el tiempo de ejecución
start_time = datetime.now()

t = 0
for n in range(1, LIMITE + 1):
    t += n ** n

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0036:", str(t)[-10:]
