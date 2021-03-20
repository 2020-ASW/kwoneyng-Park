def tsp(vis, cur):
    global ans
    if dp[cur][vis]:
        return dp[cur][vis]

    if vis == (1<<n)-1:
        #완수
        if arr[cur][0]:
            return arr[cur][0]
        return 1e9

    rs = 1e9
    for nxt in range(n):
        if arr[cur][nxt] and not vis & 1<<nxt:
            rs = min(tsp(vis+(1<<nxt), nxt) + arr[cur][nxt], rs)
    dp[cur][vis] = rs
    return dp[cur][vis]
            
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(1<<n) for _ in range(n)]

print(tsp(1,0))