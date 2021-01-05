from heapq import heappop, heappush

n,m = map(int,input().split())
narr = [[] for _ in range(n+1)]
S = 1
T = 2

for i in range(m):
    a,b,c = map(int,input().split())
    narr[a].append([c,b])
    narr[b].append([c,a])

dt = [9999999]*(n+1)

q = []
heappush(q,[0,2])
dt[2] = 0
dp = [0]*(n+1)
dp[2] = 1
while q:
    val, node = heappop(q)
    val *= -1
    for nv, nxt in narr[node]:
        nv -= val
        if nv < dt[nxt]:
            dt[nxt] = -nv
            heappush(q,[-nv,nxt]) 
        if dt[nxt] < val:
            dp[node] += dp[nxt]

print(dt)
print(dp)