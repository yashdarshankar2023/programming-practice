a = "hheellooaaaabbbdcbbba"
temp = 0
bool1 = 0
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        temp +=1

    else:
        if(temp==0):
            print(a[i])
            bool1 = 1
            break
        else:
            temp = 0

if(bool1==0 and a[len(a)-1]!=a[len(a)-2]):
    print(a[len(a)-1])