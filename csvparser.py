def csvparser(filepath):
    namelist = []
    levellist = []
    gradelist = []
    csvobj = open(filepath, "r")
    for line in csvobj:
        rowlist = line.split(",",-1)
        namelist.append(rowlist[0])
        levellist.append(int(rowlist[1]))
        gradelist.append(int(rowlist[2]))
    csvobj.close()
    return (namelist, levellist, gradelist)
