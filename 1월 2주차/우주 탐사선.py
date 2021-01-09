def exploration(a,rs = 0,cnt = 1):
    global ans
    if cnt == n:
        ans = min(rs,ans)
        return
    for i in range(n):
        if a != i and vis[i] == 0 and rs+arr[a][i] < ans:
            vis[i] = 1
            exploration(i,rs+arr[a][i], cnt + 1)
            vis[i] = 0

n, s = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

for k in range(n):
    for x in range(n):
        for y in range(n):
            if x != y:
                arr[x][y] = min(arr[x][y], arr[x][k] + arr[k][y])

ans = 1e9
vis = [0]*n
vis[s] = 1
exploration(s)
print(ans)