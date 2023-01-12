a = "geeksforgeeks"
b = "forgeeksgeeks"

for i in range(len(a)):
    temp = a[i:] + a[:i]
    if(temp == b):
        print("rotation")
