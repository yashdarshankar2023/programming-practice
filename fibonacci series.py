n = 9
# def fibo(n):
#     if(n==1 or n==2):
#         return 1
#     elif(n==0):
#         return 0
#
#     return fibo(n-1) + fibo(n-2)
#
# print(fibo(n))
#methodh 2

n = 5
a = 0
b = 1
print(a)
print(b)
if(n==0):
    print(0)
elif(n==1):
        print(1)
else:
    for i in range(1,n):
        c = a + b
        a = b
        b = c
        print(c)
