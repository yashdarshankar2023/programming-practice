a = [1,3,5,2,2]
for i in range(len(a)):
    if(sum(a[:i])==sum(a[i+1:])):
        print(i)
