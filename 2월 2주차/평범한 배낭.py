n,k = map(int,input().split())

arr = []
ans = 0

for _ in range(n):
    arr.append(list(map(int,input().split())))

dp = [[0]*(k+1) for i in range(n)]

for i in range(n):
    w,v = arr[i]
    for j in range(k+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

# print(dp)
print(dp[-1][-1])