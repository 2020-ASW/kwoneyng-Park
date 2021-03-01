import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
rows = list(map(int,input().split()))
cols = list(map(int,input().split()))

narr = [[] for _ in range((2*n +2))]
part = n
st = 2*n
ed = 2*n+1

f = [[0]*(2*n+2) for _ in range(2*n+2)]
c = [[0]*(2*n+2) for _ in range(2*n+2)]

for i in range(n):
    narr[st].append(i)
    narr[i].append(st)
    c[st][i] = rows[i]
    narr[n+i].append(ed)
    narr[ed].append(n+i)
    c[n+i][ed] = cols[i]
    for j in range(n):
        narr[i].append(n+j)
        narr[n+j].append(i)
        c[i][n+j] = 1

while True:
    d = [-1]*(2*n+2)
    q = deque()
    q.append(st)
    while q:
        cur = q.popleft()
        for nxt in narr[cur]:
            if d[nxt] == -1 and c[cur][nxt] - f[cur][nxt] > 0:
                d[nxt] = cur
                q.append(nxt)
                if nxt == ed:
                    break
    if d[ed] == -1: break
    flow = 1e9
    s = ed
    while s != st:
        flow = min(flow, c[d[s]][s] - f[d[s]][s])
        s = d[s]

    s = ed
    while s != st:
        f[d[s]][s] += flow
        f[s][d[s]] -= flow
        s = d[s]
        
for i in range(n):
    cnt = 0
    for j in range(n,2*n):
        if f[i][j]:
            cnt += 1
    if cnt != rows[i]:
        print(-1)
        exit()

for j in range(n,n*2):
    cnt = 0
    for i in range(n):
        if f[i][j]:
            cnt += 1
    if cnt != cols[j-n]:
        print(-1)
        exit()
        
print(1)
for i in range(n):
    for j in range(n,2*n):
        if f[i][j] == 0:
            print('0',end='')
        elif f[i][j]:
            print('1',end='')
     
    print('')