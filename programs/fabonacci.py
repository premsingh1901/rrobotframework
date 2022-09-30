def fab(num):
   # 0,1,1,2,3,5,8
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(num-2):
       sum=a+b
       print(sum, end=" ")
       a=b
       b=sum



n=7
fab(n)