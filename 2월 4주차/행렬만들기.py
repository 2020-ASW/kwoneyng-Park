import sys

n = int(input())
rows = list(map(int,input().split()))
cols = list(map(int,input().split()))
ans = [[0]*n for _ in range(n)]

for x in range(n):
    for y in range(n):
        if rows[x] and cols[y]:
            rows[x] -= 1
            cols[y] -= 1
            ans[x][y] = 1

for i in ans:
    print(i)

for x in range(n):
    if rows[x]:
        