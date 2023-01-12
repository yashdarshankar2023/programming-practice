s = "i.like.this.program.very.much"
# temp = ""
# lst = []
# for i in s:
#
#     if(i=="."):
#         lst.append(temp)
#         temp = ""
#     else:
#         temp = temp + i
# lst.append(temp)
# print(lst)

s = s.split(".")
a = ""
for i in range(len(s)):
    if(i==0):
        a += s[i]
    elif(i%2!=0):
        a +=".abc"
    else:
        a += "."+s[i]

print(a)