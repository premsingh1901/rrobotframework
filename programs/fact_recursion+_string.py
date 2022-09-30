def reverse(str):
    if str == "":
        return str
    else:
        return reverse(str[1:]) + str[0]


str1 = reverse("prem singh")
print(str1)
print("=============")
str2 = "prem singh"
print(str2[::-1])

