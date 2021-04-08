def make(idx=0):
    if idx == len(blank):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=' ')
            print()
        exit()

    x,y = blank[idx]
    able = []
    for i in range(1,10):
        if row[x][i] == 0 and col[y][i] == 0:
            able.append(i)
    
    for i in able:
        row[x][i] = 1
        col[y][i] = 1
        board[x][y] = i
        make(idx+1)
        row[x][i] = 0
        col[y][i] = 0
        board[x][y] = 0



board = [list(map(int,input().split())) for _ in range(9)]

blank = []
row = [[0]*10 for _ in range(9)]
col = [[0]*10 for _ in range(9)]
for i in range(9):
    row[i][0] = 1
    col[i][0] = 1

for i in range(9):
    for j in range(9):
        if not board[i][j]:
            blank.append([i,j])
        else:
            row[i][board[i][j]] = 1
            col[j][board[i][j]] = 1

# print('==================')
make()