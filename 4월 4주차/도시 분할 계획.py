import sys
from heapq import heappop,heappush
input = sys.stdin.readline

n,m = map(int,input().split())
narr = [[] for _ in range(n+1)]
total = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    total += c
    narr[a].append((c,b))
    narr[b].append((c,a))

cost = [1e9]*(n+1)
vis = [0]*(n+1)
vis[0] = 1
vis[1] = 1
cost[0] = 0
cost[1] = 0
hq = []
heappush(hq,(0,1))
while hq:
    val, cur = heappop(hq)
    vis[cur] = 1
    for nval, nxt in narr[cur]:
        if vis[nxt] == 0 and cost[nxt] > nval:
            heappush(hq,(nval,nxt))
            cost[nxt] = nval

# print(cost)
print(sum(cost)-max(cost))