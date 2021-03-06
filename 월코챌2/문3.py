from collections import deque
import sys
sys.setrecursionlimit(300000)

def search(x,a,narr):
    global vis
    global n
    global answer
    cur = a[x]
    vis[x] = 1
    for nxt in narr[x]:
        if vis[nxt] == 0:
            cur += search(nxt,a,narr)
            
    answer += abs(cur)
    return cur

def solution(a, edges):
    global vis
    global n
    global answer
    if sum(a):
        return -1
    answer = 0
    n = len(a)
    vis = [0]*n
    narr = [[] for _ in range(n)]
    for s,e in edges:
        narr[s].append(e)
        narr[e].append(s)
    search(0,a,narr)
    
    return answer


a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
print(solution(a, edges))