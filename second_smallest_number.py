arr = [1,2,3,4,5,6]
s = 9999
s2 = 9999
for i in arr:
    if s > i:
        s = i
    elif(i>s and i<s2):
        s2 = i

print(s2)
