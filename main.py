import csvparser
import transitiongenerator
import arraycreator
import numpy
import matrixprinter
#filename1 = input("Enter the name of the first year's file:")
#filename2 = input("Enter the name of the second year's file:")
filename1 = "/Users/ryankupyn/Google Drive/Consulting Projects/NWGC Choir Size/2011 Choir students clean.csv"
filename2 = "/Users/ryankupyn/Google Drive/Consulting Projects/NWGC Choir Size/2012 Choir students clean.csv"
year1list = csvparser.csvparser(filename1)
print year1list
year2list = csvparser.csvparser(filename2)
print year2list
transitionslist = transitiongenerator.pathconstructor(year1list, year2list)
print transitionslist
choristerarray = arraycreator.arraycreator(transitionslist)
matrixprinter.matrixprinter(choristerarray)
#print choristerarray[1,2,:,:].sum()
