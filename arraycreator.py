import numpy
def arraycreator(translist):
    N = 13
    choirtransmatrix = numpy.zeros((N,)*4)
    for element in translist:
        choirtransmatrix[element[0], element[1], element[2], element[3]] += 1
    return choirtransmatrix
