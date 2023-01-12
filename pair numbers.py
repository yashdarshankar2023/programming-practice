a = [1,4,45,6,10,8]
a.sort()
print(a)
left = 0
right = len(a) - 1
x = 16
while(left < right):
    sum1 = a[left] + a[right]
    if(sum1 >  x):
        right -= 1
    elif(sum1 < x):
        left += 1
    else:
        print(x)
        left += 1
        break

    print(sum1)




