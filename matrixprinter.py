import numpy
def matrixprinter(choristerarray):
    for level1 in range(0,7):
        for year1 in range(0,13):
            totalmembers = choristerarray[level1,year1,:,:,:].sum()
            veterans = choristerarray[level1,year1,:,:,1].sum()
            newbies = choristerarray[level1,year1,:,:,0].sum()
            if totalmembers > 0:
                print("Number of students in choir " + str(level1) + " grade " + str(year1) + ": " + str(totalmembers))
                print(str(veterans) + " veterans")
                print(str(newbies) + " newbies")
                for level2 in range(0,7):
                    for year2 in range(0,13):
                        for vetlevel in range(0,2):
                            transfer = choristerarray[level1,year1,level2,year2, vetlevel]
                            if transfer > 0:
                                print("experience " + str(vetlevel) + " transfer to: " + str(level2) + " " + str(year2) + ": " + str(transfer))
                                print("probability: " + str(transfer/totalmembers))
