from collections import deque
from heapq import heappush, heappop

def solution(k, num, links):
    answer = 0
    n = len(num)
    indegree = [0]*n
    narr = [[] for _ in range(n)]
    parent = [-1]*n
    leaf = deque()
    for i in range(len(links)):
        left, right = links[i]
        if left == -1 and right == -1:
            leaf.append(i)
            continue
        if left >= 0:
            parent[left] = i
            narr[i].append(left)
            indegree[i] += 1
        if right >= 0:
            parent[right] = i
            narr[i].append(right)
            indegree[i] += 1
            
    dp = [0]*n
    while leaf:
        cur = leaf.popleft()
        dp[cur] += num[cur]
        par = parent[cur]
        if par >= 0:
            dp[par] += dp[cur]
            indegree[par] -= 1
            if indegree[par] == 0:
                leaf.append(par)
        else:
            root = cur
    k-=1
    while k:
        k -= 1
        mx = max(dp)
        idx = dp.index(mx)
        queue = deque()
        queue.append(idx)
        mn = 1e9
        midx = -1
        while queue:
            cur = queue.popleft()
            for nxt in narr[cur]:
                queue.append(nxt)
                if mx - dp[nxt] < mn:
                    midx = nxt
                    mn = mx-dp[nxt]
        val = dp[midx]

        cut = parent[midx]
        narr[cut].pop(narr[cut].index(midx))

        while parent[midx] >= 0:
            midx = parent[midx]
            dp[midx] -= val
        
    return max(dp)

k,num,links = 	3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1], [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]
print(solution(k,num,links))