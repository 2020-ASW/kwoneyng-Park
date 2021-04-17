from heapq import heappush, heappop

def solution(n, z, roads, queries):
    answer = []
    earn = {}
    already = {}
    for s,e,w in roads:
        if not earn.get(w):
            earn[w] = set()
            already[w] = set()
        earn[w].add(s)
        already[w].add(e)
    
    earnList = sorted(list(earn.keys()))
    
    hq = []
    heappush(hq,[0,0,set([0])])
    cost = [1e9]*(z**2)
    while hq:
        cnt, val, nodes = heappop(hq)
        if cost[-val] < cnt:
            continue
        else:
            cost[-val] = cnt

        for nval in earnList:
            if val - nval <= -z**2:
                break
            if earn[nval] & nodes:
                heappush(hq, [cnt+1, val-nval, already[nval]])
            else:
                heappush(hq, [cnt+2, val-nval, already[nval]])
        if val - z > -z**2:
            heappush(hq, [cnt+1, val-z, nodes])

 
    for c in queries:
        start = 0
        if c > z**2:
            c -= z
            start = c//z**2
            start *= z
            c %= z**2
            c += z
        if cost[c] >= 1e9:
            answer.append(-1)
        else:
            answer.append(cost[c] + start)
        
    return answer
    
n,z,roads,queries = 5, 5, [[1, 2, 3], [0, 3, 2]], [0,1,2,3,4,5,6]

print(solution(n, z, roads, queries))