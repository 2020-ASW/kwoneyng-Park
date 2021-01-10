from heapq import heappop, heappush

def go(a):
    if dp[a] != -1:
        return dp[a]
    if a == 2:
        return 1
    dp[a] = 0
    for nv,nxt in narr[a]:
        if dt[a] > dt[nxt]:
            dp[a] += go(nxt)
    return dp[a]

n,m = map(int,input().split())
dt = [1e9]*(n+1)
dt[2] = 0
narr = [[] for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    narr[a].append([c,b])
    narr[b].append([c,a])

q = []
heappush(q,[0,2])
while q:
    val, cur = heappop(q)
    for nval, nxt in narr[cur]:
        nval += val
        if dt[nxt] > nval:
            dt[nxt] = nval
            heappush(q,[nval, nxt])

dp = [-1]*(n+1)
print(go(1))

# 10 13
# 1 4 3
# 1 5 4
# 1 3 7
# 4 6 9
# 5 7 3
# 3 7 1
# 6 9 1
# 6 10 4
# 7 10 3
# 7 8 3
# 9 2 13
# 10 2 2
# 8 2 4
