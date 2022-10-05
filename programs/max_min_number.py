lst = [40, 10, 20, 50, 60]
# lst.sort()
# print("Max: ", lst[len(lst)-1])
# print("Max: ", lst[0])

for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i]<lst[j]:
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)



