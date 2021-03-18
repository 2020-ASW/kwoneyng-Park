from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    od = int(input())
    if od:
        heappush(heap,od)
    elif heap:
        print(heappop(heap))
    else:
        print(0)


