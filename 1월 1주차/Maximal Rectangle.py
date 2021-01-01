matrix = [["0","0","1"],["1","1","1"]]
n = len(matrix)
m = len(matrix[0])

dp = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == '1':
            dp[i][j] = 1

for i in range(n):
    for j in range(1,m):
        if dp[i][j] and dp[i][j-1]:
            dp[i][j] = dp[i][j-1]+dp[i][j]

ans = 0

def calc(dp,col,start,i,j):
    global ans
    cnt = 0
    for l in col:
        for k in range(start,i+1):
            if l <= dp[k][j]:
                cnt += 1
            else:
                ans = max(ans,cnt*l)
                cnt = 0
        if cnt:
            ans = max(ans, cnt*l)
            cnt = 0 

for j in range(m):
    col = []
    cnt = 0
    start = 0
    for i in range(n):
        if dp[i][j]:
            cnt += 1
            if dp[i][j] not in col:
                col.append(dp[i][j])
        else:
            if cnt:
                calc(dp,col,start,i,j)
                col = []
                cnt = 0
            start = i+1
    if cnt:
        calc(dp,col,start,i,j)


print(ans)