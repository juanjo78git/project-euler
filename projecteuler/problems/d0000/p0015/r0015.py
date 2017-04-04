# -*- coding: utf-8 -*-

# La solución hecha por mi mismo está en c, pero como quiero tenerlo todo
# resuelto añado una utilizando el Triángulo de Pascal

import math


def result():
    n = 40
    k = 20
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))
