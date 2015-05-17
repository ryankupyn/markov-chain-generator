def csvparser(filepath):
    namelist = []
    levellist = []
    gradelist = []
    csvobj = open(filepath, r)
    for line in csvobj:
        rowlist = line.rsplit(sep = ",")
        namelist.append(rowlist[0])
        levellist.append(rowlist[1])
        gradelist.append(rowlist[2])
    csvobj.close()
    return (namelist, levellist, gradelist)
