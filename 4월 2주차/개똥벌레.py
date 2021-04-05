import sys
input = sys.stdin.readline

n,h = map(int,input().split())

sucksoon = [0]*(h+1)
jongyousuck = [0]*(h+1)

for i in range(n):
    su = int(input())
    if i%2:
        jongyousuck[h-su+1] += 1
    else:
        sucksoon[su] += 1

# print(jongyousuck)
# print(sucksoon)
for i in range(h-1,-1,-1):
    sucksoon[i] += sucksoon[i+1]

for i in range(1,h+1):
    jongyousuck[i] += jongyousuck[i-1]

total = [0]*(h)
for i in range(h):
    total[i] += jongyousuck[i+1] + sucksoon[i+1]


mn = 1e9
cnt = 0
for i in total:
    if mn > i:
        mn = i
        cnt = 1
    elif mn == i:
        cnt += 1

# print(jongyousuck)
# print(sucksoon)
# print(total)
print(mn, cnt)
