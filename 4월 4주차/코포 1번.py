from math import sqrt
for T in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = 'NO'
    for i in arr:
        if int(sqrt(i)) < sqrt(i):
            ans = 'YES'
            break
    print(ans)
