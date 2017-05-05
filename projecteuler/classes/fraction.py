# -*- coding: utf-8 -*-

class Fraction:

    def __init__(self, n, d):
        self.n = n
        self.d = d

    def __mul__(self, other):
        return Fraction(self.n * other.n, self.d * other.d)

    def __str__(self):
        return '{}/{}'.format(self.n, self.d)

    def simplify(self):
        """ Simplificar la fracción """
        for i in range(2, min(self.n, self.d) + 1):
            completed = False
            while not completed:
                if (divmod(self.n, i)[1] == 0) and (divmod(self.d, i)[1] == 0):
                    self.n = self.n // i
                    self.d = self.d // i
                else:
                    completed = True
