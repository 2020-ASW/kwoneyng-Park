from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
hx = [-2,-1,1,2,2,1,-1,-2]
hy = [1,2,2,1,-1,-2,-2,-1]
K = int(input())
w,h = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(h)]
q = deque([[0,0,0]])
vis = [[[0]*w for _ in range(h)] for _ in range(K+1)]
vis[0][0][0] = 1
if w == 1 and h == 1:
    print(0)
    exit()
ans = 0
while q:
    ans += 1
    for _ in range(len(q)):
        jump, x, y = q.popleft()
        for p in range(4):
            xi = x+dx[p]
            yi = y+dy[p]
            if 0<=xi<h and 0<=yi<w and arr[xi][yi] == 0 and vis[jump][xi][yi] == 0:
                if xi == h-1 and yi == w-1:
                    print(ans)
                    exit()
                vis[jump][xi][yi] = 1
                q.append([jump,xi,yi])
        if jump < K:
            jump += 1
            for p in range(8):
                xi = x+hx[p]
                yi = y+hy[p]
                if 0<=xi<h and 0<=yi<w and arr[xi][yi] == 0 and vis[jump][xi][yi] == 0:
                    if xi == h-1 and yi == w-1:
                        print(ans)
                        exit()
                    vis[jump][xi][yi] = 1
                    q.append([jump,xi,yi])
print(-1)

