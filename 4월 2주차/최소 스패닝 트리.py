import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n,e = map(int,input().split())

cost = [1e9]*(n+1)
narr = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,v = map(int,input().split())
    narr[a].append([v,b])
    narr[b].append([v,a])

hq = []
cost[0] = 0
vis = [0]*(n+1)
cost[1] = 0
heappush(hq, [0,1])

while hq:
    val, cur = heappop(hq)
    vis[cur] = 1
    for nval, nxt in narr[cur]:
        if vis[nxt] == 0 and cost[nxt] > nval:
            heappush(hq, [nval, nxt])
            cost[nxt] = nval

print(sum(cost))


