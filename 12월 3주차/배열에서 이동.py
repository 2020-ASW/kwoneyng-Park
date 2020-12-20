from collections import deque

def dfs(x,y,mn,mx):
    global p
    if x == n-1 and y == n-1:
        p = True
        return 
    for i in range(4):
        xi,yi = x+dx[i], y+dy[i]
        if 0<=xi<n and 0<=yi<n and vis[xi][yi] == 0:
            vis[xi][yi] = 1
            nmn = min(mn,arr[xi][yi])
            nmx = max(mx,arr[xi][yi])
            dt = nmx - nmn
            if dt <= mid and p == False:
                dfs(xi,yi,nmn,nmx)
            vis[xi][yi] = 0

    
n = int(input())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
arr = [list(map(int,input().split())) for _ in range(n)]

l,r = 0, 200
ans = 0
vis = [[0]*n for i in range(n)]
vis[0][0] = 1
while l <= r:
    mid = (l+r)//2
    p = False
    dfs(0,0,arr[0][0],arr[0][0])
    if not p:
        l = mid + 1
    else:
        r = mid - 1

print(l)