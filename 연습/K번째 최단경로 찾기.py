from heapq import heappop, heappush

def dijk():
    vis = [k]*(n+1)
    hq = []
    hq.append([0,1])
    while hq:
        val, cur = heappop(hq)
        dp[cur][k-vis[cur]] = min(val,dp[cur][k-vis[cur]])
        if vis[cur] == 0:
            continue
        vis[cur] -= 1
        for nval, nxt in narr[cur]:
            nval += val
            heappush(hq,[nval, nxt])
    return -1

n,m,k = map(int,input().split())
narr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    narr[a].append([c,b])

dp = [[1e9]*(k+1) for i in range(n+1)]
dijk()
print(dp)