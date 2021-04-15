def solution(absolutes, signs):
    n = len(absolutes)
    answer = 0
    for i in range(n):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    
    return answer