from heapq import heappop, heappush
n,m = map(int,input())

start = 1
end = n
speed = 1

cost = [1e9]*(n+1)
cost[1] = 0
hq = []
heappush(hq, [0,n])

narr = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,l,k = map(int,input().split())
    narr[a].append([l,k,b])
    narr[b].append([l,k,b])

vis = [0]*(n+1)

while hq:
    val,cur = heappop(hq)
    for dist, slimit, nxt in narr[cur]:
        