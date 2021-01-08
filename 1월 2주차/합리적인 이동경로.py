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
dt[2] = 0
dp = [0]*(n+1)
dp[2] = 1
heappush(q,[0,2])
while q:
    val, node = heappop(q)
    val = -val
    if val > dt[node]:
        continue

    for nv, nxt in narr[node]:
        if dt[nxt] > dt[node] + nv:
            dt[nxt] = dt[node] + nv
            heappush(q,[-(nv+dt[node]),nxt])
        if dt[nxt] > val:
            print('add', 'nxt =', nxt, 'node =',node, f'dp[{nxt}] =', dp[nxt], f'dp[{node}] =', dp[node])
            dp[nxt] += dp[node]
print(dp)
print(dp[1])

