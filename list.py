MyList=[1,2,3,4,2,5,3,7]
print(MyList)
NewList=[]
for i in (MyList):
    if i not in NewList:
        NewList.append(i)
print(NewList)
    
       
