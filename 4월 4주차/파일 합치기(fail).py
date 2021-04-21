def cut(l,r):
    global ans
    if r-l == 1:
        return

    mn = 1e9
    slicing = l
    adder = prefix[r] -prefix[l]
    for i in range(l,r):
        left = prefix[i] - prefix[l]
        right = prefix[r] - prefix[i]
        if mn > abs(left-right):
            mn = abs(left-right)
            slicing = i
    ans += adder
    cut(l,slicing)
    cut(slicing,r)

for T in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    prefix = [0]*(n+1)
    for i in range(1,n+1):
        prefix[i] = prefix[i-1] + arr[i-1]
    ans = 0
    cut(0, n)
    print(ans)

