def water_paste(x,y,arr):
    for i in range(1,8,2):
        xi,yi = x+dx[i],y+dy[i]
        if 0<=xi<n and 0<=yi<n and arr[xi][yi]:
            arr[x][y] += 1


def move(clouds, arr, d, s):
    moved_clouds = []
    vis = [[0]*n for _ in range(n)]
    for x,y in clouds:
        xi,yi = (x+s*dx[d])%n, (y+s*dy[d])%n
        arr[xi][yi] += 1
        moved_clouds.append((xi,yi))
        vis[xi][yi] = 1

    for x,y in moved_clouds:
        water_paste(x,y,arr)

    next_cloudes = []
    for x in range(n):
        for y in range(n):
            if arr[x][y] >= 2 and vis[x][y] == 0:
                next_cloudes.append((x,y))
                arr[x][y] -= 2
    
    return next_cloudes

dx,dy = [0,-1,-1,-1,0,1,1,1], [-1,-1,0,1,1,1,0,-1]
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
clouds = [(n-1,0), (n-1,1), (n-2,0), (n-2,1)]
for _ in range(m):
    d,s = map(int,input().split())
    clouds = move(clouds, arr, d-1, s)

# for i in arr:
#     print(i)

ans = 0
for x in range(n):
    for y in range(n):
        ans += arr[x][y]

print(ans)