def bs(idx):
    l,r = idx+1,n-1
    mnabs = abs(arr[idx] + arr[(l+r)//2 +1])
    while l<=r:
        m = (l+r)//2
        calc = abs(arr[idx] + arr[m])
        if calc < mnabs:
            mnabs = calc
            r = m-1
        else:
            l = m+1
    




n = int(input())
arr = list(map(int,input().split()))
arr.sort()
mnabs =
for i in range(n-1):
    bs(i)