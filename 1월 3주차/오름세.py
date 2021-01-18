def solve(i):
    if not dp:
        dp.append(i)
    else:
        l,r = 0,len(dp)-1
        while l<=r:
            m = (l+r)//2
            if dp[m] >= i:
                r = m-1
            else:
                l = m+1

        if l >= len(dp):
            dp.append(i)
        else:
            dp[l] = i


while True:
    try:
        n = int(input())
        arr = list(map(int,input().split()))
        dp = []
        for i in arr:
            solve(i)
        print(len(dp))

    except:
        exit()
