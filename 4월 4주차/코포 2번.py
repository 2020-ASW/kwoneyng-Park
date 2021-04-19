nCr = [[0]*21 for _ in range(21)]
for i in range(21):
    nCr[i][0] = 1
    nCr[i][i] = 1

for i in range(1,21):
    for j in range(1,i):
        nCr[i][j] = nCr[i][j-1]*(i+1-j)//j

for T in range(int(input())):
    n,k = map(int,input().split())
