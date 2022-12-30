def patternprograms(ch,n):
    assert isinstance(ch,str),"argument will be string"
    assert isinstance(n,int),"argument will be integer"
    for i in range(1,1+n):
         print(ch*i)
    return None
inpch=input("enter char")
inpnum=int(input("enter num"))
try:
    patternprograms(inpch,inpnum)
except AssertionError as ob:
    print(ob)
    
