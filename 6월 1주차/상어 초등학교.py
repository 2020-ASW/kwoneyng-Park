import sys
input = sys.stdin.readline

dx,dy = [-1,0,1,0], [0,1,0,-1]
def like_around(x,y,n,like):
    cnt = 0
    for i in range(4):
        xi,yi = x+dx[i],y+dy[i]
        if 0<=xi<n and 0<=yi<n and arr[xi][yi] in like:
            cnt += 1
    return cnt

def blank_around(x,y,n):
    cnt = 0
    for i in range(4):
        xi,yi = x+dx[i], y+dy[i]
        if 0<=xi<n and 0<=yi<n and arr[xi][yi] == 0:
            cnt += 1
    return cnt

n = int(input())
arr = [[0]*n for _ in range(n)]
likes = {}
for _ in range(n**2):
    like = list(map(int,input().split()))
    cur = like.pop(0)
    likes[cur] = like
    lcnt = 0
    bcnt = 0
    set_location = None
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 0:
                tlike = like_around(x,y,n,like)
                tblank = blank_around(x,y,n)
                if set_location == None:
                    lcnt = tlike
                    bcnt = tblank
                    set_location = [x,y]
                elif lcnt < tlike:
                    lcnt = tlike
                    bcnt = tblank
                    set_location = [x,y]
                elif lcnt == tlike and bcnt < tblank:
                    bcnt = tblank
                    set_location = [x,y]
    x,y = set_location
    arr[x][y] = cur

ans = 0
for x in range(n):
    for y in range(n):
        tlike = like_around(x,y,n,likes[arr[x][y]])
        if tlike == 0:
            ans += 0
        elif tlike == 1:
            ans += 1
        elif tlike == 2:
            ans += 10
        elif tlike == 3:
            ans += 100
        elif tlike == 4:
            ans += 1000

print(ans)