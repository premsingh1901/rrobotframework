str="python is programing language"
search="is2"

if search in str:
    print("Found")
else:
    print("Not Found")

if str.find(search)==-1:
    print("not Found")
else:
    print("Found")

str1 = "AHCECLWLXO"
str2=str1[1::2]
print("Hello: ",str2.lower())
