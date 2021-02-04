def solution(ms):
    n = len(ms)
    dp = [[1e9]*n for i in range(n)]
    for i in range(n):
        dp[i][i] = 0
        
    for k in range(1,n):
        for s in range(n-k):
            e = k+s
            for i in range(s,e):
                dp[s][e] = min(dp[s][e], dp[s][i] + dp[i+1][e] + ms[s][0]*ms[i][1]*ms[e][1])
    
    return dp[0][n-1]