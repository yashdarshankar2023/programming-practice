a = 8
lst = []
def tobin(a):
    if(a==1 or a==0):
        lst.append(a)

    else:
        lst.append(a%2)
        tobin(a//2)
    return lst[::-1]



print(tobin(a))