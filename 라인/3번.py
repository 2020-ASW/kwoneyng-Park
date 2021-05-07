from collections import deque

def solution(ads):
    answer = 0
    ads.sort(key=lambda x:x[0])
    ads = deque(ads)
    time = ads[0][0]
    tmp = []
    while ads or tmp:
        calc = []
        while ads and ads[0][0]<=time:
            tmp.append(ads.popleft())

        if not tmp:
            t,c = ads.popleft()
            time = t
            tmp.append([t,c])
            while ads and ads[0][0]<=time:
                tmp.append(ads.popleft())
        
        for i in range(len(tmp)):
            calc.append(((time-tmp[i][0]+5)*tmp[i][1],i))
        
        calc.sort(reverse=True)
        t,c = tmp.pop(calc[0][1])
        answer += (time-t)*c
    
        time += 5
    return answer

ads = [[5, 2], [2, 2], [6, 3], [9, 2]]
print(solution(ads))