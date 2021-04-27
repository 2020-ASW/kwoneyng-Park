import sys
from collections import deque
input = sys.stdin.readline

dx,dy = [-1,0,1,0], [0,1,0,-1]

def numbering(x,y,num):
    queue = deque()
    queue.append((x,y))
    clustering[x][y] = num
    cluster[num].append((0,x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            xi,yi = x+dx[i], y+dy[i]
            if 0<=xi<n and 0<=yi<n and clustering[xi][yi] == 0 and arr[xi][yi] == 1:
                clustering[xi][yi] = num
                cluster[num].append((0,xi,yi))
                queue.append((xi,yi))

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

clustering = [[0]*n for _ in range(n)]
cnt = 0
cluster = {}
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and clustering[i][j] == 0:
            cnt += 1
            cluster[cnt] = deque()
            numbering(i,j,cnt)
ans = 1e9

distance = [[1e9]*n for _ in range(n)]

for num in range(1,cnt+1):
    queue = cluster[num]
    while queue:
        val,x,y = queue.popleft()
        for i in range(4):
            xi,yi = x+dx[i], y+dy[i]
            if 0<=xi<n and 0<=yi<n:
                if clustering[xi][yi] == num:
                    continue
                elif clustering[xi][yi] > 0:
                    ans = min(ans,val)
                elif val < distance[xi][yi]:
                    distance[xi][yi] = val
                    queue.append((val+1,xi,yi))

print(ans)