def find(cur):
    if not narr[cur]:
        return dp[cur]
    child = []
    for nxt in narr[cur]:
        child.append(find(nxt))

    child.sort(reverse=True)
    for i in range(len(narr[cur])):
        child[i] += i+1
    
    dp[cur] = max(child)
    return dp[cur]


n = int(input())
arr = list(map(int,input().split()))
narr = [[] for i in range(n)]

for i in range(n):
    if arr[i] >= 0:
        narr[arr[i]].append(i)

dp = [0]*n
find(0)
print(dp)
print(dp[0])