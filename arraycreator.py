def arraycreator(translist):
    choirtransmatrix = numpy.zeros(7, 13, 7, 13)
    for element in translist:
        choirtransmatrix[element[0], element[1], element[2], element[3]] += 1
    return choirtransmatrix
