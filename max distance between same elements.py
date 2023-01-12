arr = [1,1,2,2,2,1]
left = 0
right = 1
max1 = -99
lst = []
dict1 = {}
while(left < len(arr)):
    for right in range(left+1,len(arr)):
        if(arr[left]==arr[right]):
            lst.append(right-left)

    left += 1

print(max(lst))

