import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def union(a,b):
    pa = find(a)
    pb = find(b)
    if pa > pb:
        parent[pa] = pb
    else:
        parent[pb] = pa

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


n,m = map(int,input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    order,a,b = map(int,input().split())
    if order:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a,b)
