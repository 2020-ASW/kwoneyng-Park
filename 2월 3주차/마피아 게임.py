import sys
from collections import deque
input = sys.stdin.readline

def dfs(x):
    if vis[x]:
        return
    vis[x] = 1
    if not parr[x]:
        mafia[x] = 1
        return
    for pre in parr[x]:
        dfs(pre)
        if mafia[pre] == 1:
            mafia[x] = 0
    
    nxt = narr[x]
    if mafia[nxt] == 1:
        mafia[x] = 0
    
    if mafia[x] == -1:
        mafia[x] = 1
        mafia[narr[x]] = 0
        for pre in parr[x]:
            mafia[pre] = 0

    dfs(nxt)


n = int(input())
narr = [0]*(n+1)
parr = [[] for _ in range(n+1)]
for i in range(1,n+1):
    narr[i] = int(input())
    parr[narr[i]].append(i)
    
vis = [0]*(n+1)
mafia = [-1]*(n+1)
ans = 0

for i in range(1,n+1):
    dfs(i)

# print(mafia)
print(mafia.count(1))