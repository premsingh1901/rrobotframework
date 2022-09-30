f1=open("read_file.txt", 'r')
red= f1.read()
f1.close()
f=open("write_here", 'a')
str="prem Singh "
# f.write(str)
f.writelines(str)
f.writelines()
f.writelines(red)

f.close()
