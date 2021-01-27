from math import log2

x,k = map(int,input().split())
bitn = int(log2(x))+1
cnt = 0
ans = 0

for i in range(int(log2(k))+1):
    while (x & 1<<cnt):
        cnt += 1
    if k & 1<<i:
        ans += 1<<cnt
    cnt += 1
        
print(ans)
