# 2시 55분
from collections import deque
from sys import flags

def auto():
    global ans
    vis = [[[0]*n for _ in range(n)] for _ in range(m+1)]
    groups = []
    for x in range(n):
        for y in range(n):
            if vis[arr[x][y]][x][y] == 0 and arr[x][y] > 0:
                groups.append(bfs(vis,x,y))
    
    if len(groups) == 0:
        print(ans)
        exit()
    groups.sort(reverse=True)
    if groups[0][0] < 2:
        print(ans)
        exit()

    cnt,_,x,y = groups[0]
    ans += cnt**2
    delete(x,y)
    gravity()
    rotate()
    gravity()
    auto()

def bfs(vis,x,y):
    queue = deque()
    queue.append((x,y))
    row = x
    col = y
    color = arr[x][y]
    cnt = 1
    rainbow = 0
    vis[color][x][y] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            xi,yi = x+dx[i], y+dy[i]
            if 0<=xi<n and 0<=yi<n and vis[color][xi][yi] == 0:
                if arr[xi][yi] == 0:
                    rainbow += 1
                    cnt += 1
                    queue.append((xi,yi))
                    vis[color][xi][yi] = 1
                elif arr[xi][yi] == color:
                    if row > xi:
                        row = xi
                    elif row == xi and col > yi:
                        col = yi
                    cnt += 1
                    queue.append((xi,yi))
                    vis[color][xi][yi] = 1
    return (cnt, rainbow, row, col)

def delete(x,y):
    queue = deque()
    queue.append((x,y))
    color = arr[x][y]
    arr[x][y] = -2
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            xi,yi = x+dx[i], y+dy[i]
            if 0<=xi<n and 0<=yi<n and (arr[xi][yi] == 0 or arr[xi][yi] == color):
                arr[xi][yi] = -2
                queue.append((xi,yi))

def gravity():
    stack = []
    for j in range(n):
        for i in range(n):
            if arr[i][j] == -1:
                ii = i-1
                while stack:
                    arr[ii][j] = stack.pop()
                    ii -= 1
            elif arr[i][j] >= 0:
                stack.append(arr[i][j])
                arr[i][j] = -2
        ii = n-1
        while stack:
            arr[ii][j] = stack.pop()
            ii -= 1
    return arr

def rotate():
    global arr
    narr = []
    for j in range(n-1,-1,-1):
        row = []
        for i in range(n):
            row.append(arr[i][j])
        narr.append(row)
    arr = [i[:] for i in narr]


dx,dy = [-1,0,1,0], [0,1,0,-1]
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = 0
auto()

