def sort_b(lst):
    l=len(lst)
    for i in range(l):
        for j in range(l-1):
            if lst[j]>lst[j+1]:
                temp=lst[j]
                lst[j]=lst[j+1]
                lst[j + 1]=temp
lst=[10,3,4,6,9,25]
sort_b(lst)
print(lst)