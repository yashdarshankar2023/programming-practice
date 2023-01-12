a = [[1, 1, 1 ,0, 0,],[ 0, 1, 0, 0, 0,], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
n = 5
m = 5
lst = []
for i in range(n-2):
    for j in range(m-2):
        sum1 = a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]
        lst.append(sum1)


print(max(lst))