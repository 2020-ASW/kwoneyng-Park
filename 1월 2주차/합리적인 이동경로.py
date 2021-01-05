from heapq import heappop, heappush

def go(a,b):
    q = []
    q.append([0,a])
    vis = [0]*(n+1)
    vis[a] = 1
    while q:
        val, node = heappop(q)
        if node == b:
            return val
        for nval, nxt in narr[node]:
            if vis[nxt] == 0:
                vis[nxt] = 1
                nval += val
                heappush(q,[nval,nxt])

def find(a):
    if dp[a] != -1:
        return dp[a]
    if a == 2:
        dp[a] = 1
        return 1
    
    dp[a] = 0
    for nv, nxt in narr[a]:
        if dt[nxt] < dt[a]:
            dp[a] += find(nxt)
    return dp[a]

n,m = map(int,input().split())
narr = [[] for _ in range(n+1)]
S = 1
T = 2

for i in range(m):
    a,b,c = map(int,input().split())
    narr[a].append([c,b])
    narr[b].append([c,a])

dt = [0]
for i in range(1, n+1):
    dt.append(go(i,2))


dp = [-1]*(n+1)
print(find(1))

print(dt)
print(dp)