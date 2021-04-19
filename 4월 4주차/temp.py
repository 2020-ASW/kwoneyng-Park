import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

if m == 1:
    for i in arr:
        for j in i:
            print(-j, end=' ')
        print()
    exit()

tarr = [[0]*n for _ in range(n)]
totalx = [[0]*n for _ in range(n)]
bomb = [[0]*n for _ in range(n)]
half = m//2

for i in range(half,n-half):
    for j in range(half,n-half):
        if j < m:
            if j == half:
                tarr[i][j] = -arr[i-half][j-half]
                totalx[i][j] = tarr[i][j]
            else:
                tarr[i][j] = -arr[i-half][j-half] + arr[i-half][j-half-1]
                totalx[i][j] = tarr[i][j] + totalx[i][j-1]
        else:
            tarr[i][j] = -totalx[i][j-1] + totalx[i][j-m] - arr[i-half][j-half]
            totalx[i][j] = tarr[i][j] + totalx[i][j-1]

# for i in tarr:
#     print(i)

totaly = [[0]*n for _ in range(n)]

for j in range(half,n-half):
    for i in range(half,n-half):
        if i < half+m:
            bomb[i][j] = tarr[i][j] - tarr[i-1][j]
            totaly[i][j] = bomb[i][j] + totaly[i-1][j]
        else:
            bomb[i][j] = totaly[i-m][j] - totaly[i-1][j] + tarr[i][j]
            totaly[i][j] = bomb[i][j] + totaly[i-1][j]

# for i in bomb:
#     print(i)

for i in bomb:
    print(' '.join(map(str,i)))