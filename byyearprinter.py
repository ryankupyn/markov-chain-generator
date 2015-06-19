import numpy
def matrixprinter(choristerarray):
    for year1 in range(0,13):
        totalmembers = choristerarray[:,year1,:,:,:].sum()
        veterans = choristerarray[:,year1,:,:,1].sum()
        newbies = choristerarray[:,year1,:,:,0].sum()
        if totalmembers > 0:
            print("Number of students in  grade " + str(year1) + ": " + str(totalmembers))
            print(str(veterans) + " veterans")
            print(str(newbies) + " newbies")
            for year2 in range(0,13):
                for vetlevel in range(0,2):
                    transfer = choristerarray[:,year1,:,year2, vetlevel].sum()
                    if transfer > 0:
                        print("experience " + str(vetlevel) + " transfer to: " + str(year2) + ": " + str(transfer))
                        print("probability: " + str(transfer/choristerarray[:,year1,:,:, vetlevel].sum()))
