n = int(input())
arr = list(map(int,input().split()))
m = int(input())

prefix = [0]*(n+1)
for i in range(n):
    prefix[i+1] = arr[i] + prefix[i]

amount = [0]*(n)

for i in range(n):
    if i+m <= n:
        amount[i] = prefix[i+m] - prefix[i]
    else:
        amount[i] = prefix[-1] - prefix[i]

dp = [[0]*n for _ in range(3)]
dp[0][0] = amount[0]

for i in range(1,n):
    dp[0][i] = max(dp[0][i-1], amount[i])

for i in range(1,3):
    for j in range(m*i,n):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-m]+amount[j])

    
# print(amount)
# for i in dp:
#     print(i)
print(dp[-1][-1])