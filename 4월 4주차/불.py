from collections import deque

dx,dy = [-1,0,1,0], [0,1,0,-1]
for T in range(int(input())):
    m,n = map(int,input().split())
    arr = [list(input()) for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '@':
                start = (i,j)
                arr[i][j] = '.'
            elif arr[i][j] == '*':
                queue.append((i,j))
    vis = [[0]*m for _ in range(n)]
    ans = 0
    flag = False
    vis[start[0]][start[1]] = 1
    queue.append(start)

    while queue:
        ans += 1
        for _ in range(len(queue)):
            x,y = queue.popleft()
            for i in range(4):
                xi,yi = x+dx[i], y+dy[i]
                if 0<=xi<n and 0<=yi<m and arr[xi][yi] == '.' and vis[xi][yi] == 0:
                    vis[xi][yi] = 1
                    