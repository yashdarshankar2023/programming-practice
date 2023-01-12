arr = [0,0,1,1,0]
lst = []
for i in arr:
    if(i==0):
        lst = [0] + lst
    else:
        lst = lst + [1]
        
print(lst)