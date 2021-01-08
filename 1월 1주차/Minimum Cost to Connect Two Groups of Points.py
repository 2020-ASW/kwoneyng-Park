import sys
from functools import lru_cache

cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]

@lru_cache(None)
def solve(index ,mask):
    if index == size1:
        ans2 = 0
        for j in range(size2):
            if (mask & (1<<j)) == 0:
                ans2+=mincost[j]
        return ans2
    ans = sys.maxsize
    for j in range(size2):
        ans = min(ans,cost[index][j] + solve(index+1 , mask | (1<<j)))
    return ans
size1 = len(cost)
size2 = len(cost[0])
mincost = [sys.maxsize]*size2
for j in range(size2):
    for i in range(size1):
        mincost[j] = min(mincost[j] , cost[i][j])
print(solve(0,0))
