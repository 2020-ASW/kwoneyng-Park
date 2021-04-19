import sys
from collections import deque
input = sys.stdin.readline

for T in range(int(input())):
    n,d,c = map(int,input().split())
    narr = [[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int,input().split())
        narr[b].append([s,a])

    cost = [1e9]*(n+1)
    queue = deque()
    queue.append([0,c])
    cost[c] = 0
    while queue:
        val, cur = queue.popleft()
        for nval, nxt in narr[cur]:
            nval += val
            if cost[nxt] > nval:
                cost[nxt] = nval
                queue.append([nval, nxt])

    cnt = 0
    mx = 0
    for i in range(1,n+1):
        if cost[i] < 1e9:
            cnt += 1
            mx = max(mx, cost[i])

    print(cnt, mx)