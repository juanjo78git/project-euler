def p100(n):
    salida = False
    nf = float(n)
    while salida == False:
        d = 4 - 8*(nf - (nf ** 2))
        rd = float(d) ** 0.5
        if int(rd) == rd:
            r = (2 + float(rd))/float(4)
            if int(r) == r:
                print "Resultado: ", int(r), int(n)
                salida = True
        n = n + 1
        if n % 10000000 == 0:
            print n

