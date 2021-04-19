from collections import deque
n,t = map(int,input().split())
dungeon = []
for idx in range(n):
    a,b = map(int,input().split())
    dungeon.append([a,b])


arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

dp = [[0]*(t+1) for _ in range(n)] # dp[사냥터][시간]

for i in range(n):
    if dungeon[i][0] == 0:
        exp = dungeon[i][1]
        for j in range(1,t+1):
            dp[i][j] = dp[i][j-1] + exp

for i in range(n):
    need = dungeon[i][0]
    exp = dungeon[i][1]
    for j in range(n):
        for k in range(n):
            if i == k:
                continue
            if dp[k][j] > need and j+arr[i][k] <= t:
                dp[i][j+arr[i][k]] = max(dp[i][j+arr[i][k]], dp[k][j] + exp)

for i in dp:
    print(i)