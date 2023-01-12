a = [1,0,0,2,2,1,0]
low = 0
mid = 0
high = len(a) - 1
temp = 0
while(mid<=high):
    if(a[mid]==0):
        temp = a[low]
        a[low] = a[mid]
        a[mid] = temp
        low += 1
        mid += 1

    elif(a[mid]==1):
        mid += 1

    else:
        temp = a[high]
        a[high] = a[mid]
        a[mid] = temp
        high -= 1


print(a)