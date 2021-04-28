import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
narr = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
hq = []
times = [0]*(n+1)
for i in range(1,n+1):
    data = list(map(int,input().split()))
    cost = data[0]
    indegree[i] = len(data) - 2
    if indegree[i] == 0:
        heappush(hq,(cost,i))
        times[i] = cost
    for j in range(1,len(data)-1):
        narr[data[j]].append((cost,i))


while hq:
    time, cur = heappop(hq)
    for ntime, nxt in narr[cur]:
        ntime += time
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heappush(hq,((ntime,nxt)))
        times[nxt] = max(times[nxt],ntime)

for i in times[1:]:
    print(i)