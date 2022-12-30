def printmonth(dn):
    if (dn==1):
        da= "january"
    elif(dn==2):
        da= "feb"
    elif(dn==3):
        da= "march"
    elif(dn==4):
        da= "april"
    elif(dn==5):
       da= "may"
    elif(dn==6):
        da= "june"
    return da
def printmonth1(dn):
    if (dn==1):
        da= "sunday"
    elif(dn==2):
        da= "monday"
    elif(dn==3):
        da= "tuesday"
    elif(dn==4):
        da= "wednesday"
    elif(dn==5):
       da= "thursday"
    elif(dn==6):
        da= "friday"
    return da
import time
for i in range(3):
    inpnum=int(input())
    start=time.time()
    print(printmonth(inpnum))
    print((time.time()-start)*100000)
    start=time.time()
    print(printmonth1(inpnum))
    print((time.time()-start)*100000)
    
