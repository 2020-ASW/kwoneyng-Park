n = int(input())
arr = list(map(int,input().split()))

arr.sort()

mn = 1e11
ans = []
for i in range(n-2):
    l,r = i+1, n-1
    while l < r:
        tsum = arr[i] + arr[r] + arr[l]
        if mn > abs(tsum):
            mn = abs(tsum)
            ans = [arr[i], arr[l], arr[r]]
        if tsum > 0:
            r -= 1
        elif tsum < 0:
            l += 1
        else:
            print(ans)
            exit()

print(ans)