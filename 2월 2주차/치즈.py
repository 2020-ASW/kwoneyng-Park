from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def spreadAir():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 2

    q = deque()
    q.append([0,0])
    arr[0][0] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            xi,yi = x+dx[i], y+dy[i]
            if 0<=xi<n and 0<=yi<m and arr[xi][yi] == 2:
                q.append([xi,yi])
                arr[xi][yi] = 0


def meltingCheese():
    global cheese
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 1:
                cnt = 0
                for i in range(4):
                    xi,yi = x+dx[i], y+dy[i]
                    if 0<=xi<n and 0<=yi<m and arr[xi][yi] == 0:
                        cnt += 1
                if cnt > 1:
                    cheese-=1
                    arr[x][y] = 2

n,m = map(int,input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int,input().split())))

cheese = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cheese += 1
        else:
            arr[i][j] = 2
time = 0
while cheese:
    spreadAir()
    meltingCheese()
    time += 1
print(time)