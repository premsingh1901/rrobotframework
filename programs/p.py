

def fact(num):
    n = 0
    n1 = 1
    print(n)
    print(n1)
    while num >= 3:
        sum = n + n1
        # if sum>50:
        #     break
        print(sum)
        n = n1
        n1 = sum
        num-=1


num1=int(input("Enter the number: "))
fact(num1)