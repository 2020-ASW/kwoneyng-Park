from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(m, arr):
    n = len(arr)
    if arr[0][0] > m:
        return False
    q = deque()
    q.append([0,0])
    vis = [[0]*n for _ in range(n)]
    vis[0][0] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            xi = x+dx[i]
            yi = y+dy[i]
            if 0<=xi<n and 0<=yi<n and vis[xi][yi] == 0 and arr[xi][yi] <= m:
                vis[xi][yi] = 1
                q.append([xi,yi])
                if xi == n-1 and yi == n-1:
                    return True
    return False
    

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        l,r =  0, n*n-1
        while l<=r:
            m = (l+r)//2
            if bfs(m,grid):
                r = m-1
            else:
                l = m+1
        return l
        