a = "abbaabbaa"
#
# b = a[::-1]
# if(a==b):
#     print("it is palindrome")
# else:
#     print("it is not palindrome")
#

#methodh 2
res = 0
for i in range(len(a)):
    if(a[i]!=a[len(a)-i-1]):
        res = 1

print(res)


