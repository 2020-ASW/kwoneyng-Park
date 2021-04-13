import sys
input = sys.stdin.readline

def mark_left(idx):
    flag = True
    for i in range(idx-1,-1,-1):
        if arr[i] < arr[idx]:
            left[idx] = max(left[i]+1,left[idx])
            flag = False
    if flag:
        left[idx] = 1
    
def mark_right(idx):
    flag = True
    for i in range(idx+1,n):
        if arr[i] < arr[idx]:
            right[idx] = max(right[i]+1,right[idx])
            flag = False
    if flag:
        right[idx] = 1


n = int(input())
arr = list(map(int, input().split()))

left = [0]*n
right = [0]*n

for i in range(n):
    mark_left(i)

for i in range(n-1,-1,-1):
    mark_right(i)

ans = 0
for i in range(n):
    ans = max(left[i]+right[i] - 1, ans)

print(ans)