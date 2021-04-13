n,k = map(int,input().split())

arr = [[0]*n for _ in range(n)]
for _ in range(k):
    a,b = map(lambda x:int(x)-1,input().split())
    arr[a][b] = -1
    arr[b][a] = 1

for k in range(n):
    for x in range(n):
        for y in range(n):
            if x != y:
                if arr[x][k] == arr[k][y] and arr[x][k]:
                    arr[x][y] = arr[x][k]


s = int(input())
for _ in range(s):
    a,b = map(lambda x:int(x)-1, input().split())
    print(arr[a][b])