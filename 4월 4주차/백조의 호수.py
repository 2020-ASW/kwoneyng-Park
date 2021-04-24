import sys
from collections import deque
from heapq import heappush,heappop

input = sys.stdin.readline

def dijik(swan):
    s,e = swan
    sx,sy = s
    ex,ey = e
    cost = [[1e9]*m for _ in range(n)]
    cost[sx][sy] = 0
    queue = []
    queue.append((0,sx,sy))
    while queue:
        t,x,y = heappop(queue)
        if x==ex and y==ey:
            return t
        for i in range(4):
            xi,yi = x+dx[i], y+dy[i]
            if 0<=xi<n and 0<=yi<m and cost[xi][yi] > t:
                cost[xi][yi] = t
                heappush(queue,(max(dp[xi][yi],t),xi,yi))
    


dx,dy = [-1,0,1,0], [0,1,0,-1]
n,m = map(int,input().split())

arr = []
for i in range(n):
    arr.append(list(input()))
vis = [[0]*m for i in range(n)]

dp = [[1e9]*m for i in range(n)]

xque = deque()
swan = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            swan.append((i,j))
        if arr[i][j] != 'X' and vis[i][j] == 0:
            queue = deque()
            queue.append((i,j))
            dp[i][j] = 0
            while queue:
                x,y = queue.popleft()
                for p in range(4):
                    xi,yi = x+dx[p], y+dy[p]
                    if 0<=xi<n and 0<=yi<m and vis[xi][yi] == 0:
                        if arr[xi][yi] != 'X':
                            queue.append((xi,yi))
                            vis[xi][yi] = 1
                            dp[xi][yi] = 0
                        else:
                            vis[xi][yi] = 1
                            xque.append((2,xi,yi))
                            dp[xi][yi] = 1
                            
for t,x,y in xque:
    vis[x][y] = 1

while xque:
    t,x,y = xque.popleft()
    for i in range(4):
        xi,yi = x+dx[i], y+dy[i]
        if 0<=xi<n and 0<=yi<m and dp[xi][yi] > t:
            dp[xi][yi] = t
            xque.append((t+1,xi,yi))


print(dijik(swan))