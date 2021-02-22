n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

bridge = [[1]*n for _ in range(n)]
ans = 0

for k in range(n):
    for x in range(n):
        for y in range(x,n):
            if x == k or y == k or x == y:
                continue
            if arr[x][y] == arr[x][k] + arr[k][y]:
                bridge[x][y] = 0
            elif arr[x][y] > arr[x][k] + arr[k][y]:
                print(-1)
                exit()

# for i in bridge:
#     print(i)

for x in range(n):
    for y in range(x,n):
        if bridge[x][y] == 1:
            ans += arr[x][y]

print(ans)     

