n = int(input())
arr = list(map(int,input().split()))

mx = 0
for i in range(n):
    h1 = arr[i]
    cnt = 0
    see = -1e9
    for j in range(i+1,n):
        h2 = arr[j]
        dx = j-i
        dy = h2-h1
        grad = dy/dx
        if see < grad:
            see = grad
            cnt += 1

    see = 1e9
    for j in range(i-1,-1,-1):
        h2 = arr[j]
        dx = i-j
        dy = h1-h2
        grad = dy/dx
        if see > grad:
            see = grad
            cnt += 1

    if mx < cnt:
        mx = cnt

print(mx)