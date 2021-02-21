def calc(cur, sales, narr, dp):
    dp[cur][1] = sales[cur]
    if not narr[cur]:
        dp[cur][0] = 0
        return
    flag = 0
    dt = 1e9
    for nxt in narr[cur]:
        calc(nxt, sales, narr, dp)
        if dp[nxt][1] <= dp[nxt][0]:
            flag = 1
        else:
            dt = min(dt, dp[nxt][1] - dp[nxt][0])
        dp[cur][1] += min(dp[nxt][1],dp[nxt][0])
        dp[cur][0] += min(dp[nxt][1],dp[nxt][0])
    if not flag:
        dp[cur][0] += dt
    
        

def solution(sales, links):
    n = len(sales)
    narr = [[] for _ in range(n)]
    for cur, nxt in links:
        narr[cur-1].append(nxt-1)
    dp = [[0]*2 for i in range(n)]
    calc(0,sales,narr,dp)
    return min(dp[0][0], dp[0][1])