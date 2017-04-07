# -*- coding: utf-8 -*-

import os

class Sudoku:
    """Un sudoku!!"""
    def __init__(self, cadena):
        self.__sudoku = []
        for i in range(len(cadena)):
            self.__sudoku.append(int(cadena[i]))

    #def __str__(self):
    #       return self."
    def __str__(self):
        s = ""
        for i in range(9):
            if i % 3 == 0:
                s += "+-----+-----+-----+\n"
            for j in range(9):
                if j % 3 == 0:
                    s += "|"
                s += str(self.__sudoku[(i*9)+j])
                if (j+1) % 3 != 0:
                    s += " "

                if (j+1) % 9 == 0:
                    s += "|"

            s += "\n"
        s += "+-----+-----+-----+"
        return s

    # @TODO: porfavor, hay que limpiar este metodo
    def getpossibles(self, i):
        """ devuelve la lista de posibles! """
        if self.__sudoku[i] != 0:
            return []

        c, i, j = self.getcord(i)
        #cubo = self.getcube(c)
        fila = self.getfile(i)
        columna = self.getcolumn(j)

        miss = self.getmissnumcube(c)
        poss = list(miss)

        for m in miss:
            if m in fila or m in columna:
                poss.remove(m)
        return poss

    def getcord(self, i):
        """ retorna las cordenadas """
        # @TODO repasar, que python3 no me gusta mucho lo de dividir :(
        cubo = ((i//27) * 3 + (i//3) % 3)
        fila, columna = divmod(i, 9)
        return cubo, fila, columna

    def getfile(self, n):
        """ devuelve la fila n """
        return self.__sudoku[(9*n):((9*n)+9)]

    def getmissnumcube(self, n):
        """ mira que numero falta en el cubo n """
        miss = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        cube = self.getcube(n)
        for i in range(9):
            if cube[i] != 0:
                miss.remove(int(cube[i]))
        return miss

    def getcolumn(self, n):
        """ le paso una columna de la 0 a la 8 y me devuelve los datos... """
        column = []
        for j in range(9):
            column.append(self.__sudoku[n+(j*9)])

        return column

    def getcube(self, n):
        """ le paso uno de los cubos y devuelve los datos que tiene... """
        cubo = []
        for f in range(3):
            for i in range(3):
                e = (27 * (n / 3)) + (f * 9) + i + ((n % 3) * 3)
                cubo.append(self.__sudoku[e])
        return cubo

    def is_valid_partial(self, partial):
        """ si una linea, cubo y columna es valida """
        complet = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in partial:
            if i != 0:
                if i not in complet:
                    return False
                else:
                    complet.remove(i)
        return True

    def is_valid(self):
        """ si es valido, no si es solucion """
        for i in range(9):
            if not self.is_valid_partial(self.getcube(i)):
                return False
            if not self.is_valid_partial(self.getcolumn(i)):
                return False
            if not self.is_valid_partial(self.getfile(i)):
                return False
        return True

    def is_solved_partial(self, partial):
        partial.sort()
        if [1, 2, 3, 4, 5, 6, 7, 8, 9] == partial:
            return True
        else:
            False

    def is_solved(self):
        """ si es solucion """
        for i in range(9):
            if not self.is_solved_partial(self.getcube(i)):
                return False
            if not self.is_solved_partial(self.getcolumn(i)):
                return False
            if not self.is_solved_partial(self.getfile(i)):
                return False
        return True

    # funciona!, pero no me esta guardando el resultado :_(
    def resolve(self):
        if self.is_solved():
            return True
        else:
            # buscamos el primer 0 libre
            for i in range(81):
                if self.__sudoku[i] == 0:
                    break
            # para cada uno de los elementos posibles, llamo recursivamente
            for p in self.getpossibles(i):
                self.__sudoku[i] = p
                if self.is_valid():
                    if not self.resolve():
                        self.__sudoku[i] = 0
                    else:
                        return True
                else:
                    self.__sudoku[i] = 0
            return False

    def getcornerleft(self):
        return int(str(self.__sudoku[0]) + str(self.__sudoku[1])
                   + str(self.__sudoku[2]))


def result():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    fichero = os.path.join(ROOT_DIR, 'sudoku.txt')

    lsudoku = []
    f = open(fichero)
    i = 0
    s = ''
    for l in f:
        if i == 0:
            i += 1
            continue
        elif i < 10:
            s = s + l.replace('\n', '').replace('\r', '')

        if i % 10 == 0:
            i = 0
            lsudoku.append(Sudoku(s))
            s = ''
        i += 1

    lsudoku.append(Sudoku(s))

    total = 0
    i = 0
    # print(len(lsudoku))
    for sudoku in lsudoku:
        # print(i)
        sudoku.resolve()
        total += sudoku.getcornerleft()
        i += 1

    # print("Solucion 0096:", total)
    return total
