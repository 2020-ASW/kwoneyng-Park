import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
tarr = [[0]*n for _ in range(n)]
totalx = [[0]*n for _ in range(n)]
bomb = [[0]*n for _ in range(n)]
half = m//2

for i in range(n-m+1):
    for j in range(n-m+1):
        xi,yi = i+half, j+half
        if j < m:
            if j == 0:
                tarr[xi][yi] = -arr[i][j]
                totalx[xi][yi] = tarr[xi][yi]
            else:
                tarr[xi][yi] = -arr[i][j] + arr[i][j-1]
                totalx[xi][yi] = tarr[xi][yi] + totalx[xi][yi-1]
        else:
            tarr[xi][yi] = -totalx[xi][yi-1] + totalx[xi][yi-m] - arr[i][j]
            totalx[xi][yi] = tarr[xi][yi] + totalx[xi][yi-1]

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