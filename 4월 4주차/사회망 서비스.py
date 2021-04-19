import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

narr = [[] for _ in range(n+1)]
for i in range(n-1):
    u,v = map(int,input().split())
    narr[u].append(v)
    narr[v].append(u)

dp = [[0,1] for _ in range(n+1)]
vis = [0]*(n+1)

stack = deque([1])
parent = [0]*(n+1)

leaf = deque()
indegree = [0]*(n+1)

while stack:
    cur = stack.pop()
    vis[cur] = 1
    for nxt in narr[cur]:
        if vis[nxt]:
            continue
        parent[nxt] = cur
        indegree[cur] += 1
        if len(narr[nxt]) == 1:
            leaf.append(nxt)
        else:
            stack.append(nxt)
        
while leaf:
    cur = leaf.popleft()
    if cur == 1:
        break
    nxt = parent[cur]
    dp[nxt][0] += dp[cur][1]
    dp[nxt][1] += min(dp[cur][0], dp[cur][1])
    indegree[nxt] -= 1
    if indegree[nxt] == 0:
        leaf.append(nxt)

print(min(dp[1][0], dp[1][1]))