from collections import deque
def solution(n, edges):
    answer = 0
    narr = [[] for _ in range(n+1)]
    for s,e in edges:
        narr[s].append(e)
        narr[e].append(s)
        
    q = deque()
    vis = [0]*(n+1)
    q.append(1)
    vis[1] = 1
    while q:
        tail = []
        for _ in range(len(q)):
            node = q.popleft()
            tail.append(node)
            for nxt in narr[node]:
                if vis[nxt] == 0:
                    vis[nxt] = 1
                    q.append(nxt)
    start = tail[0]
    q.append(start)
    vis = [0]*(n+1)
    vis[start] = 1
    depth = 0
    while q:
        depth+=1
        ctail = len(q)
        for _ in range(len(q)):
            node = q.popleft()
            for nxt in narr[node]:
                if vis[nxt] == 0:
                    vis[nxt] = 1
                    q.append(nxt)
    if len(tail) > 1 or ctail > 1:
        return depth - 1
    else:
        return depth - 2