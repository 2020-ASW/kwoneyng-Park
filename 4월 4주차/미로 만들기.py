from heapq import heappop,heappush

n = int(input())
arr = [list(input()) for _ in range(n)]
dx,dy = [-1,0,1,0], [0,1,0,-1]

hq = []
vis = [[1e9]*n for _ in range(n)]
vis[0][0] = 0


heappush(hq,(0,0,0))
while hq:
    cnt,x,y = heappop(hq)
    for i in range(4):
        xi,yi = x+dx[i], y+dy[i]
        if 0<=xi<n and 0<=yi<n and vis[xi][yi] > cnt:
            vis[xi][yi] = cnt
            if arr[xi][yi] == '0':
                heappush(hq,(cnt+1,xi,yi))
            else:
                heappush(hq,(cnt,xi,yi))

# for i in vis:
#     print(i)

print(vis[-1][-1])
