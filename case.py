s=input("enter a string")
lc=0
uc=0
for i in s:
    if (i.islower()):
       lc=lc+1
    else:
        uc=uc+1
print(lc)
print(uc)
