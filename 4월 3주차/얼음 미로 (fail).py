import sys
input = sys.stdin.readline

from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
w,h = map(int,input().strip().split())

arr = []
for i in range(h):
    arr.append(list(input().strip()))

cost = [[1e9]*w for _ in range(h)]
for x in range(h):
    for y in range(w):
        if arr[x][y] == 'T':
            tera = [x,y]
            cost[x][y] = 0
            arr[x][y] = 0
        elif arr[x][y] == 'E':
            ext = [x,y]
        elif arr[x][y].isdigit():
            arr[x][y] = int(arr[x][y])

def move(val, x, y, p):
    px = dx[p]
    py = dy[p]
    go = 0
    while True:
        x += px
        y += py
        if 0<=x<h and 0<=y<h:
            if arr[x][y] == 'R':
                x -= px
                y -= py
                val += go
                if cost[x][y] > val and go:
                    queue.append([val,x,y])
                    cost[x][y] = val
                return

            elif arr[x][y] == 'H':
                return
            elif arr[x][y] == 'E':
                val += go
                cost[x][y] = min(val, cost[x][y])
                return
            else:
                go += arr[x][y]
        else:
            return


queue = deque()
queue.append([0]+tera)
while queue:
    val, x, y = queue.popleft()
    for cmd in range(4):
        move(val,x,y,cmd)


print(cost[ext[0]][ext[1]] if cost[ext[0]][ext[1]] < 1e9 else -1)