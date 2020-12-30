from collections import deque
dx,dy = [-1,0,1,0], [0,1,0,-1]

for T in range(1,int(input())+1):
    n,m,k = map(int,input().split())
    mx = n + k + 1
    my = m + k + 1
    arr = [[0]*my for _ in range(mx)]
    vis = [[0]*my for _ in range(mx)]
    q = deque()
    ans = 0
    for i in range(n):
        data = list(map(int,input().split()))
        for j in range(m):
            if data[j] > 0:
                xi, yi = i+k//2, j+k//2
                arr[xi][yi] = data[j]
                q.append([xi,yi,data[j]])
                vis[xi][yi] = 1
                ans += 1
    
    for _ in range(k):
        sprd = []
        for _ in range(len(q)):
            x,y,g = q.popleft()
            if arr[x][y] > 0:
                arr[x][y] -= 1
                if arr[x][y] == 0:
                    arr[x][y] = g*(-1)
            elif arr[x][y] < 0:
                if vis[x][y] == 1:
                    for p in range(4):
                        xi,yi = x+dx[p], y+dy[p]
                        if vis[xi][yi] == 0:
                            if [xi,yi] not in sprd:
                                sprd.append([xi,yi])
                            arr[xi][yi] = max(arr[xi][yi],g)
                arr[x][y] += 1
                vis[x][y] = -1
            
            if arr[x][y] != 0:
                q.append([x,y,g])
            else:
                ans -= 1
        
        for i, j in sprd:
            q.append([i,j,arr[i][j]])
            vis[i][j] = 1
            ans += 1
    print(f'#{T} {ans}')
