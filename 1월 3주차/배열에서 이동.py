from collections import deque

def bfs(m):
    for k in range(mn,mx-m+1):
        clear()
        makeMap(k,m)
        if vis[0][0] == 1 or vis[n-1][n-1] == 1:
            continue
        q = deque([[0,0]])
        while q:
            x,y = q.popleft()
            if x == n-1 and y == n-1:
                return True
            for p in range(4):
                xi,yi = x+dx[p], y+dy[p]
                if 0<=xi<n and 0<=yi<n and vis[xi][yi] == 0:
                    vis[xi][yi] = 1
                    q.append([xi,yi])
    return False


def clear():
    for x in range(n):
        for y in range(n):
            vis[x][y] = 0

def makeMap(k,m):
    for x in range(n):
        for y in range(n):
            if arr[x][y] < k:
                vis[x][y] = 1
            elif arr[x][y] >= k and arr[x][y] <= k+m:
                vis[x][y] = 0
            else:
                vis[x][y] = 1

n = int(input())
dx,dy = [-1,0,1,0], [0,1,0,-1]
vis = [[0]*n for i in range(n)]
arr = [list(map(int,input().split())) for _ in range(n)]
mx = 0
mn = 200
for i in range(n):
    for j in range(n):
        t = arr[i][j]
        mx = max(t, mx)
        mn = min(t,mn)


l,r = 0,mx-mn
while l<=r:
    m = (l+r)//2
    if bfs(m):
        r = m-1
    else:
        l = m+1
print(l)
    