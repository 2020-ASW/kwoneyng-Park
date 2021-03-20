n = int(input())
su = {}
sarr = list(map(int,input().split()))
ans = 0

sufsum = [0]*60001
presum = [0]*60001

for i in range(n):
    if i >= 2:
        sufsum[sarr[i]] += 1

presum[sarr[0]] += 1
for i in range(1,n-1):
    for j in range(2*sarr[i]+1):
        ans += presum[j] * sufsum[sarr[i]*2 - j]

    presum[sarr[i]] += 1
    sufsum[sarr[i+1]] -= 1
    
print(ans)