import sys
sys.setrecursionlimit(10000)
def dfs(cur):
    vis[cur] = 1
    dp[0][cur] = 0
    dp[1][cur] = arr[cur]
    for nxt in narr[cur]:
        if vis[nxt]:
            continue
        dfs(nxt)
        dp[0][cur] += max(dp[1][nxt], dp[0][nxt])
        dp[1][cur] += dp[0][nxt]

n = int(input())
arr = [0]+list(map(int,input().split()))
narr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = sorted(map(int,input().split()))
    narr[a].append(b)
    narr[b].append(a)

vis = [0]*(n+1)
dp = [[0]*(n+1) for i in range(2)]

dfs(1)
print(max(dp[0][1], dp[1][1]))