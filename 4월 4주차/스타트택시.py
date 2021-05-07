from collections import deque


dx,dy = [-1,0,1,0], [0,1,0,-1]
n,m,k = map(int,input().split())
arr = [list(map(int, input().split())) for i in range(n)]
x,y = map(lambda x:int(x)-1, input().split())
vis = [[[0]*400 for _ in range(n)] for _ in range(n)]

people = 2
customer = {}
for i in range(m):
    a,b,c,d = map(lambda x:int(x)-1, input().split())
    arr[a][b] = people
    customer[people] = (c,d)
    people += 1

cur = 0
queue = deque()
queue.append((x,y))

while queue and k:
    k -= 1
    son = []
    for _ in range(len(queue)):
        x,y = queue.popleft()
        for i in range(4):
            xi,yi = x+dx[i], y+dy[i]
            if 0<=xi<n and 0<=yi<n and arr[xi][yi] != 1 and vis[xi][yi][cur] == 0:
                vis[xi][yi][cur] = 1
                if arr[xi][yi] > 1:
                    son.append((xi,yi,arr[xi][yi]))
                else:
                    queue.append((xi,yi))
    if son:
        son.sort()
        x,y,cur = son[0]
        ex,ey = customer[cur]
        queue = deque()
        queue.append((x,y))
        while queue
        m -= 1

