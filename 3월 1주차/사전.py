n,m,k = map(int,input().split())
dp = [[1]*102 for _ in range(102)]
for i in range(1,102):
    dp[i][1] = i+1
    dp[1][i] = i+1

for i in range(1,102):
    for j in range(2,102):
        dp[i][j] = dp[i][j-1] * (i+j) // j
        dp[j][i] = dp[i][j]

if k > dp[n][m]:
    print(-1)
    exit()
if k == dp[n][m]:
    ans ='z'*m + 'a'*n
    print(ans)
    exit()
      
ans = ['a']*n + ['z']*m
k -= 1
total = n+m

while m:
    if k == 0:
        break
    ans[total - m] = 'a'

    for i in range(1,n+1):
        if k < dp[m][i]:
            k -= dp[m][i-1]
            ans[total-m-i] = 'z'
            break
    m-=1

print(''.join(ans))