n = int(input())
arr = [list(input()) for _ in range(n)]

for i in arr:
    print(i)

vis = [[0]*n for _ in range(n)]
