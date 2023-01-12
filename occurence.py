diction = {}
s = "aabbccdddeeeeeaabbcaba"
for i in s:
    if i not in diction.keys():
        diction[i] = 1
    else:
        diction[i] = diction[i] + 1

print(diction)
