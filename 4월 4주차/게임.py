from collections import deque

def dfs(cur):
    global cycle
    if cycle:
        return -1
    if dp[cur]:
        return dp[cur]
    vis[cur] = 1
    for nxt in narr[cur]:
        if vis[nxt] == 0:
            vis[nxt] = 1
            dp[cur] = max(dp[cur], dfs(nxt)+1)
            vis[nxt] = 0
        else:
            cycle = True
            return -1

    if dp[cur] == 0:
        dp[cur] = 1

    return dp[cur]



dx, dy = [-1,0,1,0], [0,1,0,-1]
n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
narr = [[] for _ in range(n*m)]
for x in range(n):
    for y in range(m):
        if arr[x][y] == 'H':
            continue
        su = int(arr[x][y])
        for i in range(4):
            xi,yi = x+dx[i]*su, y+dy[i]*su
            if 0<=xi<n and 0<=yi<m and arr[xi][yi] != 'H':
                narr[m*x+y].append(m*xi+yi)

vis = [0]*(n*m)
dp = [0]*(n*m)
cycle = False
dfs(0)
if cycle:
    print(-1)
else:
    print(dp[0])
