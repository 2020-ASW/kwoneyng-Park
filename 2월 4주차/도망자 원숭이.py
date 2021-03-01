import sys
input = sys.stdin.readline

n,m,q = map(int,input().split())
bullying = list(map(int,input().split()))
bullying = [1e9] + bullying
arr = [[1e9]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,d = map(int,input().split())
    arr[a][b] = d+max(bullying[a], bullying[b])
    arr[b][a] = d+max(bullying[a], bullying[b])

for k,v in sorted(enumerate(bullying), key=lambda x:x[1]):
    if k == 0: continue
    for x in range(1,n):
        for y in range(1,n):
            temp = min(max(bullying[x],bullying[k]), max(bullying[k],bullying[y]))
            if arr[x][y] > arr[x][k] + arr[k][y] - temp :
                arr[x][y] = arr[x][k] + arr[k][y] - temp

for _ in range(q):
    a,b = map(int,input().split())
    print(arr[a][b] if arr[a][b] < 1e9 else -1)