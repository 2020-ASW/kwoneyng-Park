def dc(i):
    if i > dp[-1]:
        dp.append(i)
        return
    l,r = 0,len(dp)
    while l <= r:
        mid = (l+r)//2
        if i > dp[mid]:
            l = mid + 1
        else:
            r = mid - 1
    dp[l] = i


ans = 1
while True:
    try:
        n = int(input())
        arr = list(map(int,input().split()))
        dp = [0]
        for i in arr:
            dc(i)
        print(len(dp)-1)

    except Exception:
        break