mat = [[6,5,4],[1,2,5],[7,9,7]]
sum1 = 0
sum2 = 0
for i in range(len(mat)):
    for j in range(i,len(mat)):

        sum2 += mat[len(mat)-1-i][len(mat)-1-j]
        sum1 += mat[i][j]

print(sum1,sum2)