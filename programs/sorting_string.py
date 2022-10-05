lst_str=["prem", "shuchi", "hitu", "apple"]
print(lst_str)
# lst_str.sort()
lst=[]
for str in lst_str:
    str1=str[::-1]
    print(str1)
    lst.append(str1)

l=len(lst_str)-1
lst2=[]
while l>=0:
    lst2.append(lst_str[l])
    l-=1
print("Reversed by logic: {}".format(lst2))


lst_str.reverse()
print("Reverese: {}".format(lst_str))
print(lst_str)
print(lst)