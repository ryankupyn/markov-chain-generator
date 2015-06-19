import csvparser
import transitiongenerator
import arraycreator
import numpy
import matrixprinter
startyear = input("Enter the starting year")
endyear = input("Enter the ending year")
referenceyear = "/Users/ryankupyn/Google Drive/Consulting Projects/NWGC Choir Size/" + str(startyear-1) + " Choir students clean.csv"
filename1 = "/Users/ryankupyn/Google Drive/Consulting Projects/NWGC Choir Size/" + str(startyear) + " Choir students clean.csv"
filename2 = "/Users/ryankupyn/Google Drive/Consulting Projects/NWGC Choir Size/"+ str(endyear) + " Choir students clean.csv"
referenceyearlist = csvparser.csvparser(referenceyear)
year1list = csvparser.csvparser(filename1)
print year1list
year2list = csvparser.csvparser(filename2)
print year2list
transitionslist = transitiongenerator.pathconstructor(year1list, year2list, referenceyearlist)
print transitionslist
choristerarray = arraycreator.arraycreator(transitionslist)
matrixprinter.matrixprinter(choristerarray)
