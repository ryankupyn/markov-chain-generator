import numpy
def arraycreator(translist):
    N = 13
    choirtransmatrix = numpy.zeros((N,)*5)
    for element in translist:
        choirtransmatrix[element[0], element[1], element[2], element[3], element[4]] += 1
    return choirtransmatrix
