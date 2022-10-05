# print("enter the num: ")
# n = int(input())
num=100
plst=[]
nplst=[]
for n in range(2,num):
    j = 2
    while j <= n//2:
        if n % j == 0:
            plst.append(n)
            break
        j += 1
    else:
        nplst.append(n)

print("Not Prime: ", plst)
print("Prime: ", nplst)

num1=int(input("Enter the number: "))
for num in range(1, num1):
    for i in range(2, num):
        if num%i==0:
            # print("Not Prime")
            break
    else:
        print(num, "Prime")




