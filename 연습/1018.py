def checkWB(sx,sy):
    ans = 1e9
    for white in range(2):
        cnt = 0
        for x in range(8):
            for y in range(8):
                if arr[sx+x][sy+y] != check[(x+y)%2 - white]:
                    cnt += 1
        ans = min(cnt, ans)
    return ans

n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(input()))

check = ['W','B']
mn = 1e9
for i in range(n-7):
    for j in range(m-7):
        mn = min(mn, checkWB(i,j))

print(mn)

# def checkWB(sx,sy):
#     white = 0
#     if arr[sx][sy] != 'W':
#         white = 1
#     cnt = 0
#     for x in range(8):
#         for y in range(8):
#             if arr[sx+x][sy+y] != check[(x+y)%2 - white]:
#                 cnt += 1
#                 if cnt > mn:
#                     return cnt
#     return cnt

# n,m = map(int,input().split())
# arr = []
# for i in range(n):
#     arr.append(list(input()))

# check = ['W','B']
# mn = 1e9
# for i in range(n-7):
#     for j in range(m-7):
#         mn = min(mn, checkWB(i,j))
#         if mn == 12:
#             print(i,j)

# print(mn)