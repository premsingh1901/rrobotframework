def fact(num):
    if num == 0:
        return 1
    f= num * fact(num - 1)
    return f


fct = fact(5)
print(fct)
