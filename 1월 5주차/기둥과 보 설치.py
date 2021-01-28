def solution(n, build_frame):
    answer = []

    def is_col_possible(x, y):
        if y == 0:
            return True
        elif x > 0 and 1 in board[x - 1][y]:
            return True
        elif 0 in board[x][y - 1]:
            return True
        elif 1 in board[x][y]:
            return True
        else:
            return False

    def is_bow_possible(x, y):
        if y > 0 and 0 in board[x][y - 1]:
            return True
        elif y > 0 and x < n and 0 in board[x + 1][y - 1]:
            return True
        elif 0 < x < n and 1 in board[x - 1][y] and 1 in board[x + 1][y]:
            return True
        else:
            return False

    board = [[[] for c in range(n + 1)] for r in range(n + 1)]

    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]

        if b == 1:
            if a == 0:
                if is_col_possible(x, y):
                    board[x][y].append(0)

            else:
                if is_bow_possible(x, y):
                    board[x][y].append(1)

        else:
            if a == 0:
                board[x][y].remove(0)
                if y < n and 0 in board[x][y+1]:
                    if is_col_possible(x, y+1):
                        pass
                    else:
                        board[x][y].append(0)
                        continue
                if y < n and 1 in board[x][y+1]:
                    if is_bow_possible(x, y+1):
                        pass
                    else:
                        board[x][y].append(0)
                        continue
                if x > 0 and y < n and 1 in board[x-1][y+1]:
                    if is_bow_possible(x-1, y+1):
                        pass
                    else:
                        board[x][y].append(0)
                        continue

            else:
                board[x][y].remove(1)
                if x > 0 and 1 in board[x-1][y]:
                    if is_bow_possible(x-1, y):
                        pass
                    else:
                        board[x][y].append(1)
                        continue
                if x < n and 1 in board[x+1][y]:
                    if is_bow_possible(x+1, y):
                        pass
                    else:
                        board[x][y].append(1)
                        continue
                if x < n and 0 in board[x+1][y]:
                    if is_col_possible(x+1, y):
                        pass
                    else:
                        board[x][y].append(1)
                        continue
                if 0 in board[x][y]:
                    if is_col_possible(x, y):
                        pass
                    else:
                        board[x][y].append(1)
                        continue

    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(len(board[i][j])):
                answer.append([i, j, board[i][j][k]])

    answer.sort()

    return answer