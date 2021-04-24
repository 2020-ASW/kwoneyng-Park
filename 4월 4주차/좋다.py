n = int(input())
arr = list(map(int,input().split()))
ht = {}
cnt = {}
for i in range(n):
    cnt[arr[i]] = cnt.get(arr[i],0) + 1

for i in range(n-1):
    for j in range(i+1,n):
        if arr[i] == 0 and arr[j] == 0 and cnt[0] > 2:
            key = arr[i] + arr[j]
            ht[key] = 1
        if arr[i] == 0 and arr[j] != 0 and cnt[arr[j]] > 1:
            key = arr[i] + arr[j]
            ht[key] = 1
        elif arr[j] == 0 and arr[i] != 0 and cnt[arr[i]] > 1:
            key = arr[i] + arr[j]
            ht[key] = 1
        elif arr[i] != 0 and arr[j] != 0:
            key = arr[i] + arr[j]
            ht[key] = 1

ans = 0 
for i in range(n):
    if ht.get(arr[i]):
        ans += 1

print(ans)
