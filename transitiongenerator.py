def pathconstructor(year1, year2):
    gen pairlist = []
    transitionslist = []
    for hop in year1[0]:
        if hop in year2[0]:
            pairlist.append([year1[0].index(hop), year2[0].index(hop)])
        else:
            pairlist.append([year1[0].index(hop), "out"])
    for skip in pairlist:
        if skip[1] != "out":
            transitionslist.append([year1[1][skip][0], year1[2][[skip][1]], [year2[1][skip][1], year2[2][skip]][1]])
        else:
            transitionslist.append([[year1[1][skip][0], year1[2][[skip][1]], 7, 13])
    return transitionslist
