MyList=list()
number=int(input("how many value u want to enter"))
for i in range(number):
    value=int(input("enter the value"))
    MyList.append(value)

print(MyList)
m=1
for i in(MyList):
    m=m*i
print(m)
