from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, L):
    q = deque(start)
    for i in start:
        spend[i] = time[i]
    while q:
        cur = q.popleft()
        t = spend[cur]
        for nxt in narr[cur]:
            indegree[nxt] -= 1
            spend[nxt] = max(t+time[nxt], spend[nxt])
            if indegree[nxt] == 0:
                q.append(nxt)

for T in range(int(input())):
    n,k = map(int,input().split())
    time = [0] + list(map(int,input().split()))
    narr = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    spend = [0]*(n+1)
    for _ in range(k):
        s,e = map(int,input().split())
        narr[s].append(e)
        indegree[e] += 1
    L = int(input())
    start = []
    for i in range(1,n+1):
        if indegree[i] == 0:
            start.append(i)
    bfs(start, L)
    print(spend[L])