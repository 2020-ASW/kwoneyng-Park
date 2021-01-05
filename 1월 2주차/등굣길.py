def go(x,y,arr,dp,dx,dy):
    n = len(dp)
    m = len(dp[0])
    if x == n-1 and y == m-1:
        dp[x][y] = 1
        return dp[x][y]
    dp[x][y] = 0
    for i in range(2):
        xi = dx[i] + x
        yi = dy[i] + y
        if 0<=xi<n and 0<=yi<m and arr[xi][yi] == 0:
            if dp[xi][yi] != -1:
                dp[x][y] += dp[xi][yi]
            else:
                dp[x][y] += go(xi,yi,arr,dp,dx,dy)
    return dp[x][y]

def solution(m, n, puddles):
    dx = [1,0]
    dy = [0,1]
    arr = [[0]*m for i in range(n)]
    for x,y in puddles:
        arr[x-1][y-1] = 1
    dp = [[-1]*m for i in range(n)]
    return go(0,0,arr,dp,dx,dy)
    

m,n,p = 4, 3, [[2, 2]]
print(solution(m,n,p))