import sys
from math import log2
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find(a,b):
    mn,mx = 1e7,0
    if depth[a] != depth[b]:
        for i in range(maxLevel-1,-1,-1):
            if depth[dp[a][i][0]] >= depth[b]:
                mn = min(mn,dp[a][i][1])
                mx = max(mx,dp[a][i][2])
                a = dp[a][i][0]
    
    if a == b:
        print(mn,mx)
        return

    for i in range(maxLevel-1,-1,-1):
        if dp[a][i][0] != dp[b][i][0] and dp[a][i][0] != 0 and dp[b][i][0] != 0:
            mn = min(mn,dp[a][i][1],dp[b][i][1])
            mx = max(mx,dp[a][i][2],dp[b][i][2])
            a = dp[a][i][0]
            b = dp[b][i][0]
    mn = min(mn,dp[a][0][1],dp[b][0][1])
    mx = max(mx,dp[a][0][2],dp[b][0][2])
    print(mn, mx)
    return

def makeDP(cur, par, val=0):
    depth[cur] = depth[par] + 1
    dp[cur][0][0] = par
    dp[cur][0][1] = min(dp[cur][0][1], val)
    dp[cur][0][2] = max(dp[cur][0][2], val)

    for i in range(1,maxLevel):
        jump = dp[cur][i-1]
        dp[cur][i][0] = dp[jump[0]][i-1][0]

    for nval, nxt in narr[cur]:
        if nxt != par:
            makeDP(nxt, cur, nval)

n = int(input())
narr = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,val = map(int,input().split())
    narr[a].append([val, b])
    narr[b].append([val,a])

maxLevel = int(log2(n)) + 1
dp = [[[0,1e7,0] for i in range(maxLevel)] for i in range(n+1)]
# dp[node][jump][0:node, 1:min, 2:max]
depth = [-1]*(n+1)
makeDP(1,0)
for i in range(1,maxLevel):
    for j in range(1,n+1):
        jump = dp[j][i-1][0]
        dp[j][i][1] = min(dp[j][i-1][1], dp[jump][i-1][1])
        dp[j][i][2] = max(dp[j][i-1][2], dp[jump][i-1][2])


# for i in dp:
#     print(i)

k = int(input())
for _ in range(k):
    a,b = map(int,input().split())
    if depth[a] < depth[b]:
        find(b,a)
    else:
        find(a,b)
