str1="prem pr pre"
str=str1.replace(" ","" )
print(str1)
l=len(str)
lst=[]
for item in str :
    count=0
    if item not in lst:
        count=str.count(item)
        print(item, ": Freq", count)
        lst.append(item)
else:
    print("Finised")



