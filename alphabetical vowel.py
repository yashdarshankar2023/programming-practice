a = "aeizxcvou"
temp = "a"
res = 0
for i in a:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        if(i >= temp):
            temp = i


        else:
            res = 1

if(res==0):
    print('success')
else:
    print("failure")