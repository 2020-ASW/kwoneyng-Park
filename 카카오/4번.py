from heapq import heappop, heappush

def solution(n, start, end, roads, traps):
    tdict = {}
    for i in traps:
        tdict[i] = 1
    narr = [[[] for _ in range(n+1)] for _ in range(2)]
    for s,e,v in roads:
        narr[0][s].append((v,e))
        narr[1][e].append((v,s))
    hq = []
    hq.append((0,0,start))
    cost = [[1e9]*(n+1) for _ in range(2)]
    while hq:
        val, stat, cur = heappop(hq)
        if cur == end:
            return val
        for nval, nxt in narr[stat][cur]:
            nval += val
            if tdict.get(nxt) == 1:
                tdict[nxt] = -1
                heappush(hq,(nval,(stat+1)%2,nxt))
            elif tdict.get(nxt) == -1:
                heappush(hq,(nval,0,nxt))
            else:
                heappush(hq,(nval,stat,nxt))
    
n,start,end,roads,traps = 4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2, 3]
print(solution(n,start,end,roads,traps))
