a = "1001"
sum1 = 0
for i,v in enumerate(a):
    if(v=="1"):
        sum1 += 2**(len(a)-1-i)

print(sum1)
