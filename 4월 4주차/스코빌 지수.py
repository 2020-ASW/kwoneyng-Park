from heapq import heappop,heappush
def solution(scoville, K):
    answer = 0
    hq = []
    for i in scoville:
        heappush(hq,i)

    while hq[0] < K:
        if len(hq) >= 2:
            answer += 1
            heappush(hq,heappop(hq)+heappop(hq)*2)
        else:
            return -1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
print(solution(scoville,7))