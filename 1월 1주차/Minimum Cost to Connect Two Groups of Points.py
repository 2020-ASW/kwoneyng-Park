cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
n = len(cost)
m = len(cost[0])

visn = [0]*n
costm = [99999]*m

for i in range(n):
    for j, cst in enumerate(cost[i]):
        costm[j] = min(costm[j], cst)

print(costm)
ans = 0

for i in range(n):
    for j in range(m):
        mn = 99999
        if cost[i][j] == costm[j]:
            visn[i] = 1
            ans += costm[j]
        else:
            mn = min(cost[i][j], mn)
    ans += mn
