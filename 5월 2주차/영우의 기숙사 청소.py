import sys
from collections import deque
input = sys.stdin.readline().strip

dx,dy = [-2,-1,1,2,2,1,-1,2], [1,2,2,1,-1,-2,-2,-1]

n,m,k,t = list(map(int, input().split()))
queue = deque()
for _ in range(m):
    x,y = map(int,input().split())
    queue.append((x,y))

clean = {}
for _ in range(k):
    x,y = map(int,input().split())
    if not clean.get(x):
        clean[x] = {}
    clean[x][y] = 1

for _ in range(k):
    for q in range(len(queue)):
        vis = {}
        x,y = queue.popleft()
        for i in range(8):
            xi,yi = x+dx[i], y+dy[i]
            if 0<=xi<n and 0<=yi<n and (not vis.get(xi) or not vis[xi].get(yi)):
                queue.append((xi,yi))
                if not vis.get(xi):
                    vis[xi] = {}
                vis[xi][yi] = 1

for x,y in queue:
    if not clean.get(x):
        continue
    elif not clean[x].get(y):
        continue
    else:
        print('YES')
        exit()

print('NO')