for T in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    prefix = [0]*(n+1)
    for i in range(1,n+1):
        prefix[i] = prefix[i-1] + arr[i-1]

    dp = [[1e9]*n for _ in range(n)]
    for i in range(n-1):
        dp[i][i+1] = arr[i] + arr[i+1]
    
    for i in range(n):
        dp[i][i] = 0

    for c in range(2,n):
        for x in range(n-c):
            y = x+c
            for k in range(x, y):
                dp[x][y] = min(dp[x][y], dp[x][k] + dp[k+1][y] + prefix[y+1] - prefix[x])

    print(dp[0][-1])

