a = [1,2,4,3,1,1,1,8,9,7,2]
a.sort()
for i in range(1,len(a)):
    if(a[i]==a[i-1]):
        print(a[i])