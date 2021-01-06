from collections import deque

grid = [['1','0']
]
n = len(grid)
m = len(grid[0])
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cluster = [[0]*m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == '1' and cluster[i][j] == 0:
            cluster[i][j] = 1
            cnt += 1
            q = deque()
            q.append([i,j])
            while q:
                x,y = q.popleft()
                for i in range(4):
                    xi,yi = x+dx[i], y+dy[i]
                    if 0<=xi<n and 0<=yi<m and cluster[xi][yi] == 0:
                        if grid[xi][yi] == '1':
                            cluster[xi][yi] = 1
                            q.append([xi,yi])
print(cnt)