import csvparser
import transitiongenerator
import arraycreator
import numpy
import byyearprinter
filedict = dict()
yeardict = dict()
transitiondict = dict()
for year in range(2008, 2015):
    filedict[year] = "/Users/ryankupyn/Google Drive/Consulting Projects/NWGC Choir Size/" + str(year) + " Choir students clean.csv"
    yeardict[year] = csvparser.csvparser(filedict[year])
for yeartran in range(2009, 2014):
    transitiondict[yeartran] = transitiongenerator.pathconstructor(yeardict[yeartran],yeardict[yeartran + 1],yeardict[yeartran-1])
print transitiondict

N = 13
choirtransmatrix = numpy.zeros((N,)*5)
for hop in transitiondict:
    for element in transitiondict[hop]:
        choirtransmatrix[element[0], element[1], element[2], element[3], element[4]] += 1
byyearprinter.matrixprinter(choirtransmatrix)
