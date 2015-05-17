import csvparser
import transitiongenerator
import arraycreator
import numpy
filename1 = input("Enter the name of the first year's file:")
filename2 = input("Enter the name of the second year's file:")
year1list = csvparser.csvparser(filename1)
print year1list
year2list = csvparser.csvparser(filename2)
print year2list
transitionslist = transitiongenerator.pathconstructor(year1list, year2list)
print transitionslist
choristerarray = arraycreator.arraycreator(transitionslist)
print choristerarray
