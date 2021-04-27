from math import ceil
n,m = map(int,input().split())
arr = list(map(int,input().split()))
mx = max(arr)
left,right = 0, ceil((n*mx)/m)+1

while left<=right:
    mid = (left+right)//2
    cnt = 0
    for i in range(m):
        cnt += mid//arr[i] + 1
    
    if cnt < n:
        left = mid+1
    else:
        right = mid-1
    
cnt = 0
for i in range(m):
    cnt += (left-1)//arr[i] + 1

nmg = n-cnt
for i in range(m):
    if left % arr[i] == 0:
        nmg -= 1
    if nmg == 0:
        print(i+1)
        break