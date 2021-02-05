def check(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

n = int(input())
order = input()

x,y = 0,0

col = [[0]*n for i in range(n)]
row = [[0]*n for i in range(n)]

for i in order:
    if i == 'U':
        nx,ny = x-1, y
    elif i == 'D':
        nx,ny = x+1,y
    elif i == 'L':
        nx,ny = x,y-1
    else:
        nx,ny = x,y+1
    
    if check(nx,ny):
        if x != nx:
            col[x][y] = 1
            x = nx
            col[x][y] = 1
        else:
            row[x][y] = 1
            y = ny
            row[x][y] = 1

ans = [['.']*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if col[i][j] and row[i][j]:
            ans[i][j] = '+'
        elif col[i][j]:
            ans[i][j] = '|'
        elif row[i][j]:
            ans[i][j] = '-'

for i in ans:
    print(''.join(i))