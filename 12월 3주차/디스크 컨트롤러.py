from heapq import heappush, heappop

def solution(jobs):
    answer = 0
    cur = 0
    n = len(jobs)
    jobs.sort()
    for i in range(len(jobs)):
        jobs[i][0], jobs[i][1] = jobs[i][1], jobs[i][0]
        
    q = []
    heappush(q, jobs.pop(0))
    while q:
        cost, at = heappop(q)
        if cur < at:
            answer += cost
            cur = at + cost
        else:
            answer += cur-at+cost
            cur += cost
        for i in range(len(jobs)):
            if cur > jobs[0][1]:
                heappush(q, jobs.pop(0))
            else:
                break
        if not q:
            if jobs:
                heappush(q, jobs.pop(0))
            
    return answer//n