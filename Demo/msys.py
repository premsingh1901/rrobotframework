lst1=[1, 22, 3, 122, 13, 123]
lst2=[1, 22, 3, 45, 13, 34]
lst3=[]
for i in lst1:
    for j in lst2:
        if i==j:
            lst3.append(i)

lst3.sort()
sl=len(lst3)-2
print(lst3[sl])
file=open("prem.txt",'w')
file.write(str(lst3[sl]))
print(lst3)


####
#search the element and return the index






