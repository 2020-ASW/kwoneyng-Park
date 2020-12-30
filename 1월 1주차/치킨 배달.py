def perm(m, st=0, cnt=0):
    global ans
    if m == cnt:
        rs = []
        cd = 0
        for i in range(c):
            if vis[i]:
                rs.append(dt[i])
        for j in range(h):
            mn = 999999
            for i in range(m):
                mn = min(mn, rs[i][j])
            cd += mn
            if cd > ans:
                return
        ans = min(cd, ans)
        return
    if m > c-st+cnt:
        return
    for i in range(st,c):
        vis[i] = 1
        perm(m,i+1,cnt+1)
        vis[i] = 0

n,m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
chick = []
home = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append([i,j])
        elif arr[i][j] == 2:
            chick.append([i,j])
c = len(chick)
h = len(home)


dt = [[0]*h for i in range(c)]

for i in range(c):
    for j in range(h):
        dt[i][j] = abs(home[j][0] - chick[i][0]) + abs(home[j][1] - chick[i][1])
vis=[0]*c
ans = 99999999
perm(m)
print(ans)

