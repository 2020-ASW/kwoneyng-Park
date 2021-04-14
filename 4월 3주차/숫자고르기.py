import sys
input = sys.stdin.readline

def pick(x):
    ivis = [0]*(n+1)
    svis = [0]*(n+1)
    while True:
        ivis[x] = 1
        svis[arr[x]] = 1
        if ivis == svis:
            for i in range(n+1):
                if ivis[i]:
                    ans[i] = 1
        if ivis[arr[x]] == 0:
            x = arr[x]
        else:
            break


n = int(input())
arr = [0]*(n+1)

for i in range(1,n+1):
    arr[i] = int(input())

ans = [0]*(n+1)

for i in range(1,n+1):
    if not ans[i]:
        pick(i)

print(sum(ans))
for i in range(1,n+1):
    if ans[i]:
        print(i)