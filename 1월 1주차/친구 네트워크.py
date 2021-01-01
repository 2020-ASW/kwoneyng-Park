import sys
input = sys.stdin.readline

def merge(a,b):
    u = find(a)
    v = find(b)
    if u == v:
        return sumset[u]
    else:
        parent[v] = u
        sumset[u] += sumset[v]
        return sumset[u]


def find(a):
    if parent[a] == a:
        return a
    
    parent[a] = find(parent[a])
    return parent[a]

for T in range(1,int(input())+1):
    f = int(input())
    ht = {}
    parent = [0]
    cnt = 1
    sumset = [0]
    for _ in range(f):
        a, b = input().split()
        if not ht.get(a):
            ht[a] = cnt
            parent.append(cnt)
            sumset.append(1)
            cnt += 1
        if not ht.get(b):
            ht[b] = cnt
            parent.append(cnt)
            sumset.append(1)
            cnt += 1
        print(merge(ht[a],ht[b]))
    
