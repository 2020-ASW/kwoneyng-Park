import sys
from heapq import heappop,heappush
input = sys.stdin.readline

def go(s):
    cost = [1e9]*(n+1)
    q = [[0,s]]
    while q:
        val, cur = heappop(q)
        if cur == x:
            gcost[s] = val
            return
        for nv, nxt in narr[cur]:
            nv += val
            if cost[nxt] > nv:
                heappush(q,[nv,nxt])
                cost[nxt] = nv

def back(e):
    q = [[0,e]]
    while q:
        val, cur = heappop(q)
        for nv, nxt in narr[cur]:
            nv += val
            if bcost[nxt]>nv:
                heappush(q,[nv,nxt])
                bcost[nxt] = nv

n,m,x = map(int,input().split())
narr =[[] for i in range(n+1)]
for _ in range(m):
    s,e,v = map(int,input().split())
    narr[s].append([v,e])

gcost = [1e9]*(n+1)
bcost = [1e9]*(n+1)
tcost = [0]*(n+1)

for i in range(1,n+1):
    if i != x:
        go(i)

back(x)

for i in range(1,n+1):
    if i == x:
        continue
    tcost[i] = gcost[i] + bcost[i]

print(max(tcost))

