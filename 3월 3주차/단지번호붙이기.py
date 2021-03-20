from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(arr,x,y):
    vis[x][y] = 1
    queue = deque()
    queue.append([x,y])
    cnt = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            xi,yi = x+dx[i], y+dy[i]
            if 0<=xi<n and 0<=yi<n and not vis[xi][yi] and arr[xi][yi]:
                cnt += 1
                vis[xi][yi] = 1
                queue.append([xi,yi])
    return cnt

n = int(input())
arr = [list(map(int,input())) for _ in range(n)]

vis = [[0]*n for _ in range(n)]
danG = []   
for i in range(n):
    for j in range(n):
        if not vis[i][j] and arr[i][j]:
            danG.append(bfs(arr,i,j))

print(len(danG))
danG.sort()
for i in danG:
    print(i)
