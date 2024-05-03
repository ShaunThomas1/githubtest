def returnValsInAscending(aList):
    if len(aList) == 0:
        return []
    else:
        print(aList[0])
        returnValsInAscending(aList[1:])

