import sys
input = sys.stdin.readline
while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    ht = {}
    ans = 0
    for i in range(n):
        ht[int(input())] = 1
    for i in range(m):
        if ht.get(int(input())):
            ans += 1
    print(ans)