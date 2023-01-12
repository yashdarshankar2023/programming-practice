s = "i like this very much "
a = ""
for i in s:
    if(i==" "):
        a += "%"
    else:
        a += i

print(a)