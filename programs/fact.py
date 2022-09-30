num=2

def fact(num):
    f = 1
    if num == 0 or num==1:
        return 1
    for i in range(1, num+1):

        f=f*i
    return f


print(fact(num))