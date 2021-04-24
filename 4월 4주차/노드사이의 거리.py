import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijik(s,e):
    cost = [1e9]*(n+1)
    hq = []
    heappush(hq,(0,s))
    cost[s] = 0
    while hq:
        val, cur = heappop(hq)
        if cur == e:
            return val
        for nval,nxt in narr[cur]:
            nval += val
            if cost[nxt] > nval:
                heappush(hq,(nval,nxt))
                cost[nxt] = nval

n,m = map(int,input().split())
narr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    narr[a].append((c,b))
    narr[b].append((c,a))

for _ in range(m):
    a,b = map(int,input().split())
    print(dijik(a,b))