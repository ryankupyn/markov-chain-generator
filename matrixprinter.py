import numpy
def matrixprinter(choristerarray):
    for level1 in range(0,7):
        for year1 in range(0,13):
            totalmembers = choristerarray[level1,year1,:,:].sum()
            if totalmembers > 0:
                print("Number of students in choir " + str(level1) + " grade " + str(year1) + ": " + str(totalmembers))
                for level2 in range(0,7):
                    for year2 in range(0,13):
                        transfer = choristerarray[level1,year1,level2,year2]
                        if transfer > 0:
                            print("transfer to: " + str(level2) + " " + str(year2) + ": " + str(transfer))
                            print("probability: " + str(transfer/totalmembers))
