from copy import deepcopy

SIZE = 6

def genPolygonals(order):
    i = 1
    while 1:
        yield i * (2  + (order - 2) * (i - 1)) / 2
        i += 1

def createFourDigitPolygonal(generator, order):
    list = []
    for x in generator(order):
        if x >= 10000:
            break
        if x >= 1000:
            list.append(x)
    return list

def getMatches(x, polygonals, available):
    matches = []
    index = 0
    for polygonal in polygonals:
        if index in available:
            for n in polygonal:
                if n / 100 == x % 100:
                    matches.append((n, index))
        index += 1
    return matches

def buildChain(chain, polygonals, available):
    if len(available):
        post = getMatches(chain[len(chain)-1], polygonals, available)
        for p in post:
            available.remove(p[1])
            chain.append(p[0])
            completeChain = buildChain(chain, polygonals, available)
            if len(completeChain) == SIZE:
                if completeChain[SIZE - 1] % 100 == completeChain[0] / 100:
                    print completeChain,
                    print sum(completeChain)
                    quit()
            chain.pop()
            available.add(p[1])
    return chain


polygonals = []
for x in range(3, SIZE + 3):
    polygonals.append(createFourDigitPolygonal(genPolygonals, x))


available = set(range(1, SIZE))


for n in polygonals[0]:
    chain = [n]
    buildChain(chain, polygonals, available)
