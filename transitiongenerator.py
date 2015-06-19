def pathconstructor(year1, year2, refyear):
    pairlist = []
    transitionslist = []
    for hop in year1[0]:
        if hop in year2[0]:
            if hop in refyear[0]:
                pairlist.append([year1[0].index(hop), year2[0].index(hop), 1])
            else:
                pairlist.append([year1[0].index(hop), year2[0].index(hop), 0])
        else:
            if hop in refyear[0]:
                pairlist.append([year1[0].index(hop), "out", 1])
            else:
                pairlist.append([year1[0].index(hop), "out", 0])
    for hop in year2[0]:
        if hop not in year1[0]:
            pairlist.append(["out", year2[0].index(hop), 0])
    for skip in pairlist:
        print skip
        if skip[0] != "out" and skip[1] != "out":
            transitionslist.append([year1[1][skip[0]], year1[2][skip[0]], year2[1][skip[1]], year2[2][skip[1]], skip[2]])
        elif skip[1] == "out":
            transitionslist.append([year1[1][skip[0]], year1[2][skip[0]], 0, 0, skip[2]])
        else:
            transitionslist.append([0, 0, year2[1][skip[1]], year2[2][skip[1]],skip[2]])
    return transitionslist
