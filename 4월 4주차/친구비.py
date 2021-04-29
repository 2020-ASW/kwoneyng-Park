def union(x,y):
    px = find(x)
    py = find(y)
    if px != py :
        mn = min(cost[px], cost[py])
        parent[py] = px
        cost[px] = mn
        cost[py] = mn


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

n,m,k = map(int,input().split())
arr = list(map(int,input().split()))
parent = [i for i in range(n+1)]
cost = [1e9]*(n+1)

for i in range(n):
    cost[i+1] = arr[i]

for i in range(m):
    v,w = map(int,input().split())
    union(v,w)

ans = 0
for i in range(1,n+1):
    px = find(i)
    if px != 0:
        ans += cost[px]
        union(0,px)

if ans <= k:
    print(ans)
else:
    print('Oh no')