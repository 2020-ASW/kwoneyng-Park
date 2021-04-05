def Union(x,y):
    px = Find(x)
    py = Find(y)
    if px != py:
        if px > py:
            px,py = py,px
        parent[py] = px
        if people[py] or people[px]:
            people[px] = 1
            people[py] = 1

def Find(x):
    if parent[x] != x:
        parent[x] = Find(parent[x])

    return parent[x]

n,m = map(int,input().split())

people = [0]*(n+1)
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i

true_people = list(map(int,input().split()))
for i in range(1,len(true_people)):
    tp = true_people[i]
    people[tp] = 1

partys = []
for _ in range(m):
    arr = list(map(int,input().split()))
    arr.pop(0)
    partys.append(arr)
    x = arr[0]
    for i in range(1,len(arr)):
        y = arr[i]
        Union(x,y)

ans = 0
for party in partys:
    for pp in party:
        if people[Find(pp)]:
            break
    else:
        ans += 1

print(ans)