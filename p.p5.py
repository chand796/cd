def printmonth(dn):
    if (dn==1):
        return "sunday"
    elif(dn==2):
        return "monday"
    elif(dn==3):
        return "tuesday"
    elif(dn==4):
        return "wednes day"
    elif(dn==5):
        return "thursday"
    elif(dn==6):
        return "friday"
    else:
        return "saturday"
for i in range(3):
    inpnum=int(input())
    print(printmonth(inpnum))
