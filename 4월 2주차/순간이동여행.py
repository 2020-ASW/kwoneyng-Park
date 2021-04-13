n,k = map(int,input().split())
mod=1000000007
dp = [0]*(n+1)
for i in range(2,n+1,2):
    dp[i]=(dp[i-2]+4**(i//2-1))%mod
for i in range(1,n+1,2):
    dp[i]=(dp[i-1]*2+1)%mod

if n%2 != k%2:
    print(dp[n])
else:
    print(dp[n]-1)
