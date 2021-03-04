def fibonacci(n,zero=0,one=0):
    if vis[n]:
        return dp[n]
    vis[n] = 1

    if n == 0:
        dp[n] = [1,0]
        return [1,0]
    if n == 1:
        dp[n] = [0,1]
        return [0,1]
    
    first = fibonacci(n-1)
    second = fibonacci(n-2)
    dp[n][0] = first[0] + second[0] 
    dp[n][1] = first[1] + second[1]
    return dp[n]


dp = [[0]*2 for _ in range(41)]
vis = [0]*41
fibonacci(40)

for T in range(int(input())):
    for i in dp[int(input())]:
        print(i, end=' ')
    print('')
