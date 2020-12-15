def pick(t):
    global ans, left, right
    if left * 2 >= total:
        ans += 2**(n-t) * fac[n-t]
        return
    else:
        for i in range(n):
            if vis[i] == 0:
                vis[i] = 1
                left += arr[i]
                pick(t+1)
                left -= arr[i]
                if left >= right + arr[i]:
                    right += arr[i]
                    pick(t+1)
                    right -= arr[i]
                vis[i] = 0
    
for T in range(1,int(input())+1):
    n = int(input())
    vis = [0]*n
    fac = [1] * (n+1)
    for i in range(1,n+1):
        fac[i] = fac[i-1]*i
    arr = list(map(int,input().split()))
    ans = 0
    total = sum(arr)
    left, right = 0, 0
    pick(0)
    print(f'#{T} {ans}')