from collections import deque

n,k,m = map(int,input().split())
if n == 1:
    print(1)
    exit()

totube = [[] for _ in range(n+1)]
tonode = [[] for _ in range(m)]
vistube = [0]*(m)
visnode = [0]*(n+1)


for i in range(m):
    data = list(map(int,input().split()))
    for j in data:
        tonode[i].append(j)
        totube[j].append(i)

q = deque()
q.append(1)
ans = 1
while q:
    ans += 1
    for i in range(len(q)):
        num = q.popleft()
        # tube로
        for nxt in totube[num]:
            if vistube[nxt] == 0:
                vistube[nxt] = 1
                q.append(nxt)
    
    for i in range(len(q)):
        num = q.popleft()
        for nxt in tonode[num]:
            if nxt == n:
                print(ans)
                exit()
            if visnode[nxt] == 0:
                visnode[nxt] = 1
                q.append(nxt)
print(-1)