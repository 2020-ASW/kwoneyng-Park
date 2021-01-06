def go(x,y,k,rs=1):
    global ans
    ans = max(rs,ans)
    vis[x][y] = 1
    for i in range(4):
        xi,yi = x+dx[i], y+dy[i]
        if 0<=xi<n and 0<=yi<n and vis[xi][yi] == 0:
            if arr[xi][yi] >= arr[x][y]:
                temp = arr[xi][yi] - arr[x][y] + 1
                if temp <= k:
                    arr[xi][yi] -= temp
                    go(xi,yi,0,rs+1)
                    arr[xi][yi] += temp
            else:
                go(xi,yi,k,rs+1)
    vis[x][y] = 0
                

dx = [-1,0,1,0]
dy = [0,1,0,-1]
for T in range(1,int(input())+1):
    ans = 0
    n,k = map(int,input().split())
    vis = [[0]*n for i in range(n)]
    arr = [list(map(int,input().split())) for i in range(n)]
    start = []
    start_max = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > start_max:
                start = []
                start_max = arr[i][j]
                start.append([i,j])
            elif arr[i][j] == start_max:
                start.append([i,j])

    for x,y in start:
        go(x,y,k)

    print(f'#{T} {ans}')
