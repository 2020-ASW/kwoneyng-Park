n, m = map(int,input().split())
arr = [list(input()) for i in range(n)]
ans = 0
for i in range(1<<n*m):
    rs = 0
    for x in range(n):
        temp = ''
        for y in range(m):
            if i & 1<<(m*x+y):
                temp += arr[x][y]
            elif temp:
                rs += int(temp)
                temp = ''
        if temp:
            rs += int(temp)

    for y in range(m):
        temp = ''
        for x in range(n):
            if not i & 1<<(m*x+y):
                temp += arr[x][y]
            elif temp:
                rs += int(temp)
                temp = ''
        if temp:
            rs += int(temp)
    ans = max(ans, rs)
print(ans)