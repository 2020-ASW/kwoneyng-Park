n = int(input())

arr = [0]*10
zero = [1]*10
for i in range(n):
    num = list(input())
    cnt = 1
    for j in range(len(num)-1,-1,-1):
        c = num[j]
        arr[ord(c)-ord('A')] += cnt
        cnt *= 10
    zero[ord(num[0])-ord('A')] = 0

mn = max(arr)
nocnt = 0

arr = list(enumerate(arr))

for i,v in arr:
    if mn > v and zero[i]:
        mn = v
        nocnt = i

arr.sort(key=lambda x:x[1], reverse=True)

start = 9
ans = 0
for i,v in arr:
    if nocnt == i:
        continue
    ans += v*start
    start -= 1
print(ans)