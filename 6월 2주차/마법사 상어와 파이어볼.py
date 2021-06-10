from collections import deque

dx,dy = [-1,-1,0,1,1,1,0,-1,], [0,1,1,1,0,-1,-1,-1]
n,m,k = map(int,input().split())
arr = [[deque() for _ in range(n)] for _ in range(n)]

queue = deque()
for i in range(1,m+1):
    x,y,w,s,d = map(int,input().split())
    x-=1; y-=1
    queue.append((x,y))
    arr[x][y].append((w,s,d))

for _ in range(k):
    vis = [[0]*n for _ in range(n)]
    for _ in range(len(queue)):
        x,y = queue.popleft()
        w,s,d = arr[x][y].popleft()
        xi,yi = x+s*dx[d], y+s*dy[d]
        xi %= n
        yi %= n
        arr[xi][yi].append((w,s,d))
        if vis[xi][yi] == 0:
            vis[xi][yi] = 1
            queue.append((xi,yi))

    for _ in range(len(queue)):
        x,y = queue.popleft()
        if len(arr[x][y]) == 1:
            queue.append((x,y))
        else:
            total_w = 0
            total_s = 0
            correct_d = True
            stdd = arr[x][y][0][2]%2
            fireL = len(arr[x][y])

            for _ in range(len(arr[x][y])):
                w,s,d = arr[x][y].popleft()
                total_w += w
                total_s += s
                if stdd != d%2:
                    correct_d = False
            
            if total_w < 5:
                continue

            if correct_d:
                for i in range(0,8,2):
                    arr[x][y].append((total_w//5, total_s//fireL,i))
                    queue.append((x,y))
            else:
                for i in range(1,8,2):
                    arr[x][y].append((total_w//5, total_s//fireL,i))
                    queue.append((x,y))

ans = 0
for i in range(n):
    for j in range(n):
        for w,s,d in arr[i][j]:
            ans += w

print(ans)


