import sys
from heapq import heappop, heappush

input = sys.stdin.readline


n,k = map(int,input().split())
gems = []
bag = []
for _ in range(n):
    m,v = map(int,input().split())
    gems.append([m,v])
for _ in range(k):
    su = int(input())
    bag.append(su)

gems.sort()
bag.sort()
idx = 0
pq = []
ans = 0

for b in bag:
    while idx < n and gems[idx][0] <= b:
        heappush(pq, -gems[idx][1])
        idx += 1
    if len(pq):
        ans -= heappop(pq)

print(ans)