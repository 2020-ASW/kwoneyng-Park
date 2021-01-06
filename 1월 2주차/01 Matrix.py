from collections import deque

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        q = deque()
        dx, dy = [0,1,0,-1], [1,0,-1,0]
        n,m = len(matrix), len(matrix[0])
        dp = [[9999]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if dp[i][j] == 9999 and matrix[i][j] == 0:
                    dp[i][j] = 0
                    dq = deque()
                    dq.append([i,j])
                    while dq:
                        x,y = dq.popleft()
                        for k in range(4):
                            xi,yi = x+dx[k], y+dy[k]
                            if 0<=xi<n and 0<=yi<m and dp[xi][yi] == 9999:
                                if matrix[xi][yi] == 0:
                                    dp[xi][yi] = 0
                                    dq.append([xi,yi])
                                else:
                                    dp[xi][yi] = 1
                                    q.append([xi,yi])
        
        cnt = 1
        while q:
            cnt += 1
            for _ in range(len(q)):
                x,y = q.popleft()
                for k in range(4):
                    xi,yi = x+dx[k], y+dy[k]
                    if 0<=xi<n and 0<=yi<m and matrix[xi][yi] == 1:
                        if cnt < dp[xi][yi]:
                            dp[xi][yi] = cnt
                            q.append([xi,yi])
                            
        return dp