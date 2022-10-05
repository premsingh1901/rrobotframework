def palindrome_bulit(s):
    s1=s[::-1]
    if s1==s:
        print("String is palindrome")
    else:
        print("String is not palindrome")

def palindrome_mycode(s1):
    l=len(s1)-1
    print(l)
    s2=""
    while l>=0:
        s2=s2+s1[l]
        l-=1
    if s1==s2:
        print("Palindrome")
    else:
        print("Not Palindrome")


def palindrome_built1(s4):
    if len(s4)==0:
        return s4
    return palindrome_built1(s4[1:])+s4[0]




str="mom"
palindrome_bulit(str)
palindrome_mycode(str)
r=palindrome_built1(str)
if r==str:
    print("Palindrome")
else:
    print("Not Palindrome")