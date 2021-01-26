import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def prim(s):
    cost = [sys.maxsize]*(v+1)
    cost[0] = 0
    cost[s] = 0
    q = []
    heappush(q,[0,s])
    while q:
        val, node = heappop(q)
        if cost[node] < val:
            continue
        for nv, nxt in narr[node]:
            nv += val
            if cost[nxt] > nv:
                cost[nxt] = nv
                heappush(q,[nv,nxt])

    return cost

v = int(input())
narr = [[] for i in range(v+1)]
for _ in range(v):
    data = list(map(int,input().split()))
    s = data.pop(0)
    data.pop()
    for i in range(len(data)//2):
        e = data[i*2]
        val = data[i*2+1]
        narr[s].append([val,e])

rs = prim(1)
start = rs.index(max(rs))
ans = prim(start)

print(max(ans))