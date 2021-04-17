import sys
input = sys.stdin.readline
n = int(input())

lines = {}

for _ in range(n):
    a,b,c = map(int,input().split())
    if b:
        gradient = a/b
    else:
        gradient = 'INF'

    if not lines.get(gradient):
        lines[gradient] = 0
    lines[gradient] += 1

ans = 0

for gradient in lines:
    ans += (n - lines[gradient]) * lines[gradient]

print(ans//2)