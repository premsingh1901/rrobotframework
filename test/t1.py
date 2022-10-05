lst=[1,1,2,3,1,4,3,8,8]
lst.sort(reverse=True)
lst1=[]
for i in lst:
    if i not in lst1:
        count=lst.count(i)
        print(i,":", count)
        lst1.append(i)
