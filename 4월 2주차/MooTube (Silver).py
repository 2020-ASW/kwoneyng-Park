from collections import deque
import sys
input = sys.stdin.readline

n,q = map(int,input().split())
narr = [[] for _ in range(n+1)]
for i in range(n-1):
    s,e,v = map(int,input().split())
    narr[s].append([v,e])
    narr[e].append([v,s])

for i in range(q):
    k,v = map(int,input().split())
    vis = [0]*(n+1)
    queue = deque()
    vis[v] = 1
    queue.append(v)
    cnt = 0
    while queue:
        cur = queue.popleft()
        for val, nxt in narr[cur]:
            if vis[nxt] == 0:
                vis[nxt] = 1
                if val >= k:
                    cnt += 1
                    queue.append(nxt)
    print(cnt)
