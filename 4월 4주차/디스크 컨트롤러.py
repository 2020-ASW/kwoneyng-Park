from heapq import heappop, heappush
from collections import deque

def solution(jobs):
    hq = []
    n = len(jobs)
    jobs.sort()
    time = 0
    jobs = deque(jobs)
    total = 0
    while jobs or hq:
        while jobs and jobs[0][0] <= time:
            t,c = jobs.popleft()
            heappush(hq,(c,t))
        if hq:
            c,t = heappop(hq)
            total += (time-t) + c
            time += c
        elif jobs:
            time = jobs[0][0]
        
    return total//n

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))