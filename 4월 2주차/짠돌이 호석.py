def rotate(arr):
    n,m = len(arr),len(arr[0])
    n,m = m,n
    narr = [[0]*m for _ in range(n)]
    for i in range(n): # 3
        for j in range(m): # 5
            narr[i][j] = arr[m-j-1][i]

    return narr

def check(sx,sy):
    for i in range(kn):
        for j in range(km):
            xi,yi = sx+i, sy+j
            if key[i][j] and Ldict.get(xi) and Ldict[xi].get(yi):
                return 1e9
    if sx < 0:
        row = max(n,sx+kn)-sx
    else:
        row = max(n,sx+kn)
    if sy <0:
        col = max(m,sy+km)-sy
    else:
        col = max(m,sy+km)
    return row*col 


n,m = map(int,input().split())

Lock = [list(map(int,list(input()))) for _ in range(n)]


kn, km = map(int,input().split())
key0 = [list(map(int,list(input()))) for _ in range(kn)]
key90 = rotate(key0)
key180 = rotate(key90)
key270 = rotate(key180)

keys = [key0, key90, key180, key270]

Ldict = {}
for i in range(n):
    for j in range(m):
        if Lock[i][j] == 1:
            if not Ldict.get(i):
                Ldict[i] = {}
            Ldict[i][j] = 1

ans = 1e9
for key in keys:
    kn,km = len(key), len(key[0])
    for i in range(-kn,n):
        for j in range(-km,m):
            ans = min(ans, check(i,j))

print(ans)