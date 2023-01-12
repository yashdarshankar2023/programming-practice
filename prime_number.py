a = 31
temp = 0
if(a==1 or a==0):
    temp = 1
for i in range(2,a):
    if(a%i==0):
        temp = 1
if(temp==1):
    print("it is not a prime number")
else:
    print("it is a prime number")