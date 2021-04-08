def rollback(arr,x):
    narr = []
    start = 2**x
    for i in range(start,n):
        narr.append(arr[i])
    while start:
        tmp = start//2
        for i in range(tmp, start):
            narr.append(arr[i])
        start = tmp
    return narr


n = int(input())
arr = list(map(int,input().split()))

idx = 0
while 2**idx < n:
    if arr[2**idx] == n:
        break
    idx += 1

b = idx
arr = rollback(arr, b)

idx = 0
while 2**idx < n:
    if arr[2**idx] == 1:
        break
    idx += 1

print(idx,b)