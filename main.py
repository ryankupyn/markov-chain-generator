import csvparser
import transitiongenerator
import arraycreator
import numpy
import matrixprinter
startyear = input("Enter the starting year")
endyear = input("Enter the ending year")
filename1 = "/Users/ryankupyn/Google Drive/Consulting Projects/NWGC Choir Size/" + str(startyear) + " Choir students clean.csv"
filename2 = "/Users/ryankupyn/Google Drive/Consulting Projects/NWGC Choir Size/"+ str(endyear) + " Choir students clean.csv"
year1list = csvparser.csvparser(filename1)
print year1list
year2list = csvparser.csvparser(filename2)
print year2list
transitionslist = transitiongenerator.pathconstructor(year1list, year2list)
print transitionslist
choristerarray = arraycreator.arraycreator(transitionslist)
matrixprinter.matrixprinter(choristerarray)
