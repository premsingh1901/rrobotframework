mylist= ["prem", "for", "prem"]
mylist1=[]
for word in mylist:
     if word not in mylist1:
        c=mylist.count(word)
        print(word, "occurance ", c)
        mylist1.append(word)
