#read
import time

file= open("G:\WorkSpcae\practice\programs\TODO", 'r')
print(file.read(10))
file.close()



#Write
file= open("G:\WorkSpcae\practice\programs\TODO", 'a')
print(file.write("Hellp"))
file.close()


currenttime= time.localtime(time.time())
print (currenttime.tm_mday)

str=" Python Language"

print(str[4: ])

d={1:"prem", 2:"hitu"}
print(d)
print(d.keys())
print(d.values())

x="45"
print(type(x))
i= int(x)
print(i)
