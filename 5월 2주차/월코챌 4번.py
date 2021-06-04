import sys
from collections import deque
sys.setrecursionlimit(100000)

def dfs(cur,narr,costs,parent):
    for nxt in narr[cur]:
        costs[cur] += dfs(nxt,narr,costs,parent)
        parent[nxt] = cur
        
    return costs[cur]
    
def solution(values, edges, queries):
    answer = []
    n = len(values)
    parent = [0]*n
    narr = [[] for _ in range(n)]
    costs = [values[i] for i in range(n)]
    for p,s in map(lambda x:[x[0]-1, x[1]-1], edges):
        parent[s] = p
        narr[p].append(s)
    
    dfs(0,narr,costs,parent)
    
    for u,w in queries:
        u-=1
        if w == -1:
            answer.append(costs[u])
        else:
            S = 0
            values[0] = 0
            while True:
                S += values[parent[u]]-values[u]
                costs[u] += S
                if u == 0:
                    break
                values[u] = values[parent[u]]
                u = parent[u]
            costs[0] += w
            values[0] = w

            
# def fix(u,parent,costs,values,w):
#     cur = u
#     d = values[u]
#     while cur != 0:
#         par = parent[cur]
#         costs[cur] -= d
#         costs[cur] += values[par]
#         values[cur] = values[par]
#         cur = par
#     costs[cur] -= d
#     costs[cur] += w
#     values[cur] = w
    
            
    print(answer)
    return answer
    

# [11111, 11010, 100, 1000, 10000, 11111, 10011, 100, 10, 10000, 11102, 10002, 100, 10, 10000]

values,edges,queries = 	[1, 10, 100, 1000, 10000], [[1, 2], [1, 3], [2, 4], [2, 5]], [[1, -1], [2, -1], [3, -1], [4, -1], [5, -1], [4, 1000], [1, -1], [2, -1], [3, -1], [4, -1], [5, -1], [2, 1], [1, -1], [2, -1], [3, -1], [4, -1], [5, -1]]
print(solution(values,edges,queries))