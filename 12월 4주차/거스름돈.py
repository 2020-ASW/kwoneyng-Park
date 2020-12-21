n = 5
money = [1,2,5]
m = len(money)
dp = [[0]*(n+1) for _ in range(m)]
for i in range(n+1):
    if i % money[0] == 0:
        dp[0][i] = 1

for i in range(1,m):
    for j in range(n+1):
        if j >= money[i]:
            dp[i][j] = dp[i-1][j] + dp[i][j-money[i]]
        else:
            dp[i][j] = dp[i-1][j]

print(dp[m-1][n])