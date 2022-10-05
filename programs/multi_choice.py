
def choice(num1, num2):
    if num1+num2==6 or num1==6 or num1-num2==6 or num2==6 or num2-num1==6:
        return True
    else:
        return False

num1=int(input("Enter first num: "))
num2=int(input("Enter second num: "))
b=choice(num1,num2)
print(b)