lst=["Prem", "Happy", "Hitu", "Prem"]
lst_new=[]
for item in lst:
    if item not in lst_new:
        count=lst.count(item)
        print(item, "= ", count )
        lst_new.append(item)
