from collections import deque
from heapq import heappop, heappush
import sys
sys.setrecursionlimit(100000)

def mark(x,y,bd,vis,cnt,near,h):
    vis[x][y] = cnt
    for a,b in near:
        xi,yi = a+x, b+y
        if 0<=xi<len(bd) and 0<=yi<len(bd) and vis[xi][yi] == -1:
            if abs(bd[x][y] - bd[xi][yi]) <= h:
                mark(xi,yi,bd,vis,cnt,near,h)

def mknxls(x,y,bd,vis,ht):
    for a,b in [[0,1],[1,0]]:
        xi,yi = a+x, b+y
    if 0 <= xi < len(bd) and 0 <= yi < len(bd):
        if vis[x][y] != vis[xi][yi]:
            nd1, nd2 = min(vis[x][y],vis[xi][yi]), max(vis[x][y], vis[xi][yi])
            if ht.get((nd1,nd2)):
                ht[(nd1,nd2)] = min(ht[(nd1,nd2)], abs(bd[x][y] - bd[xi][yi]))
            else: ht[(nd1,nd2)] = abs(bd[x][y]-bd[xi][yi])

def solution(bd, h):
    ans = 0
    q=[]
    n = len(bd)
    near = [[0,1],[1,0],[-1,0],[0,-1]]
    vis = [[-1]*n for i in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if vis[x][y] == -1:
                mark(x,y,bd,vis,cnt,near,h)
                cnt += 1
    if cnt == 1:
        return 0
    nxls = [[]for i in range(cnt)]
    ht ={}
    for x in range(n):
        for y in range(n):
            mknxls(x,y,bd,vis,ht)
    # print(ht)
    for key, val in ht.items():
        a,b = key
        nxls[a].append([val, b])
        nxls[b].append([val,a])
    heappush(q,(0,0))
    cost = [1e9]*cnt
    cost[0] = 0
    vis = [0]*cnt
    while q:
        v, n = heappop(q)
        vis[n] = 1
        for nv, nn in nxls[n]:
            if vis[nn] == 0:
                cost[nn] = min(cost[nn], nv)
                heappush(q,[nv,nn])
            
    return sum(cost)