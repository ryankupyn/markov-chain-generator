import csvparser
import transitiongenerator
import arraycreator
import numpy
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
prep1toprep2 = choristerarray[1,1,1,2]
prep1out = choristerarray[1,1,0,0]
prep1tofresca2 = choristerarray[1,1,2,2]
prep2tofresca3 = choristerarray[1,2,2,3]
prep2toprep3 = choristerarray[1,2,1,3]
prep2out = choristerarray[1,2,0,0]
prep3tofresca4 = choristerarray[1,3,2,4]
prep3out = choristerarray[1,3,0,0]
fresca2out = choristerarray[2,2,0,0]
fresca2fresca3 = choristerarray[2,2,2,3]
fresca3fresca4 = choristerarray[2,3,2,4]
fresca3amabile4 = choristerarray[2,3,3,4]
fresca3out = choristerarray[2,3,0,0]
fresca4fresca5 = choristerarray[2,4,2,5]
fresca4out = choristerarray[2,4,0,0]
fresca4amabile5 = choristerarray[2,4,3,5]
fresca5out = choristerarray[2,5,0,0]
fresca5amabile6 = choristerarray[2,5,3,6]
amabile4amabile5 = choristerarray[3,4,3,5]
amabile4out = choristerarray[3,4,0,0]
amabile5amabile6 = choristerarray[3,5,3,6]
amabile5out = choristerarray[3,5,0,0]
amabile5vivace6 = choristerarray[3,5,4,6]
amabile6amabile7 = choristerarray[3,6,3,7]
amabile6out = choristerarray[3,6,0,0]
amabile6vivace7 = choristerarray[3,6,4,7]
amabile7out = choristerarray[3,7,0,0]
amabile7vivace8 = choristerarray[3,7,4,8]
vivace6vivace7 = choristerarray[4,6,4,7]
vivace6out = choristerarray[4,6,0,0]
vivace7vivace8 = choristerarray[4,7,4,8]
vivace7out = choristerarray[4,7,0,0]
vivace8amore9 = choristerarray[4,8,5,9]
vivace8out = choristerarray[4,8,0,0]
amore9amore10 = choristerarray[5,9,5,10]
amore9ensemble10 = choristerarray[5,9,6,10]
amore9out = choristerarray[5,9,0,0]
amore10amore11 = choristerarray[5,10,5,11]
amore10ensemble11 = choristerarray[5,10,6,11]
amore10out = choristerarray[5,10,0,0]
amore11amore12 = choristerarray[5,11,5,12]
amore11ensemble12 = choristerarray[5,11,6,12]
amore11out = choristerarray[5,11,0,0]
amore12out = choristerarray[5,12,0,0]
ensemble9ensemble10 = choristerarray[6,9,6,10]
ensemble9out = choristerarray[6,9,0,0]
ensemble10ensemble11 = choristerarray[6,10,6,11]
ensemble10out = choristerarray[6,10,0,0]
ensemble11ensemble12 = choristerarray[6,11,6,12]
ensemble11out = choristerarray[6,11,0,0]
ensemble12out = choristerarray[6,12,0,0]

print choristerarray[1,2,:,:].sum()
