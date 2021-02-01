from heapq import heappop,heappush

def dijic(s,e):
    q = []
    cost = [1e10]*(n+1)
    q.append([0,s])
    while q:
        val, node = heappop(q)
        if node == e:
            return val
        for nval, nxt in narr[node]:
            nval += val
            if cost[nxt] > nval:
                cost[nxt] = nval
                heappush(q,[nval,nxt])
    return 1e10

n,e = map(int,input().split())
narr = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    narr[a].append([c,b])
    narr[b].append([c,a])

A,B = map(int,input().split())

OneToA = dijic(1,A)
OneToB = dijic(1,B)
AToB = dijic(A,B)
AToN = dijic(A,n)
BToN = dijic(B,n)

ans = min(OneToA + AToB + BToN, OneToB + AToB + AToN)
if ans >= 1e10:
    print(-1)
else:
    print(ans)