from collections import deque
dx,dy = [-1,0,1,0], [0,1,0,-1]
def solution(board):
    n = len(board)
    q = deque()
    dp = [[99999999]*n for _ in range(n)]
    q.append([0,0,0,1])
    q.append([0,0,0,2])
    dp[0][0] = 0

    while q:
        cost, x, y, p = q.popleft()
        for i in range(4):
            xi, yi = x+dx[i], y+dy[i]
            if 0<=xi<n and 0<=yi<n and board[xi][yi] == 0:
                if p == i:
                    ncst = 100+cost
                else: ncst = 600+cost
                if dp[xi][yi] >= ncst:
                    dp[xi][yi] = ncst
                    q.append([ncst, xi, yi, i])
        
    return dp[n-1][n-1]

board =	[[0, 0, 1, 0, 1, 1, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0, 1, 1, 0, 1],[1, 0, 0, 0, 0, 1, 1, 0, 1, 0],[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 1, 0, 1, 0, 1, 1],[0, 0, 1, 0, 1, 1, 0, 1, 0, 1],[0, 1, 0, 0, 1, 0, 0, 0, 1, 0],[1, 0, 0, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 1, 0, 1, 0, 0],[1, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

print(solution(board))