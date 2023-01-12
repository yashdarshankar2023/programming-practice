a = [1,2,3,4,33,44,55,77]
b = [5,6,7,8,9]
i = 0
j = 0
lst = []
while i<len(a) and j< len(b):
    lst.append(a[i])
    lst.append(b[j])
    i+=1
    j+=1

while i<len(a):
    lst.append(a[i])
    i+=1

while j < len(b):
    lst.append(b[j])
    j+=1


print("hello:",lst)