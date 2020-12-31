from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
s,b = [],[]

for i in range(n):
    a = int(input())
    if len(s) == len(b):
        heappush(s,-a)
    else:
        heappush(b,a)

    if b and -s[0] > b[0]:
        ps = -heappop(b)
        pb = -heappop(s)
        heappush(s,ps)
        heappush(b,pb)
    print(-s[0])