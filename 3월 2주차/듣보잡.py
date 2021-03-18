n,m = map(int,input().split())

ans = []
ht = {}

for i in range(n):
    name = input()
    ht[name] = 1

for i in range(m):
    name = input()
    if ht.get(name):
        ans.append(name)

ans.sort()
print(len(ans))
for i in ans:
    print(i)