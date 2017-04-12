# -*- coding: utf-8 -*-

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
# and concatenating them in any order the result will always be prime. For
# example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these
# four primes, 792, represents the lowest sum for a set of four primes with
# this property.

# Find the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.

# primess= [2,23,41,73,87]
# list(itertools.combinations(primess, 2))

# luego con esta lista solo tengo que ir cogiendo cada uno de los elementos
# y ver que tanto en un orden como en otro es un primo...


# es un número primo
def isprime(n):
    if n == 1:
        return False
    # rango empieza en 2, y solo tenemos que llegar hasta el cuadrado de n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def lprimos(n):
    """ una lista de n primos """
    nprime = 2
    primes = []
    while len(primes) != n:
        if isprime(nprime):
            primes.append(nprime)
        nprime = nprime + 1
    return primes


def concatprimes(lcomb):
    prime1 = lcomb[0]
    prime2 = lcomb[1]
    prime12 = int(str(prime1) + str(prime2))
    prime21 = int(str(prime2) + str(prime1))

    if isprime(prime12) and isprime(prime21):
        return True
    else:
        return False


def compcombinac(lxprimes, newprime):
    # llcomb = list(itertools.combinations(lxprimes, 2))

    for prime in lxprimes:
        if not concatprimes([prime, newprime]):
            return False

    # for lcomb in llcomb:
    #     if not concatprimes(lcomb):
    #         return False

    return True

def test_posible_solution(primes, newprime, current_solution):

    if current_solution:
        if sum(primes) + newprime > current_solution:
            return False

    return compcombinac(primes, newprime)


def result():

    TOTAL_PRIMES = 5000
    primes = lprimos(TOTAL_PRIMES)
    solution = None

    for pi1 in range(0, TOTAL_PRIMES-4):

        prime1 = primes[pi1]

        for pi2 in range(pi1+1, TOTAL_PRIMES-3):

            prime2 = primes[pi2]
            lp = [prime1]

            if not test_posible_solution(lp, prime2, solution):
                continue

            for pi3 in range(pi2+1, TOTAL_PRIMES-2):

                prime3 = primes[pi3]
                lp = [prime1, prime2]

                if not test_posible_solution(lp, prime3, solution):
                    continue

                for pi4 in range(pi3+1, TOTAL_PRIMES-1):

                    prime4 = primes[pi4]
                    lp = [prime1, prime2, prime3]

                    if not test_posible_solution(lp, prime4, solution):
                        continue

                    for pi5 in range(pi4+1, TOTAL_PRIMES):

                        prime5 = primes[pi5]
                        lp = [prime1, prime2, prime3, prime4]

                        if not test_posible_solution(lp, prime5, solution):
                            continue
                        else:
                            ls = [prime1, prime2, prime3, prime4, prime5]
                            solution = sum(ls)
                            # print('Possible solution: ', ls, solution)
                            

                            # exit(0)

    # print "Un resultado 0060:", sum(solution), solution
    return solution
