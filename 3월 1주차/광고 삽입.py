def parse(time):
    time = time.split(':')
    itime = int(time[0])*3600 + int(time[1])*60 + int(time[2])
    return itime

def rparse(time):
    hour = time//3600
    time %= 3600
    minute = time//60
    time %= 60
    hour = str(hour)
    minute = str(minute)
    second = str(time)
    if len(hour) < 2:
        hour = '0'+hour
    if len(minute) < 2:
        minute = '0'+minute
    if len(second) < 2:
        second = '0'+second
    return hour+':'+minute+':'+second

def solution(play_time, adv_time, logs):
    n = 100*60*60
    cnt = [0]*n
    sumarr = [0]*n
    sumcnt = [0]*n
    play_time = parse(play_time)
    adv_time = parse(adv_time)
    for log in logs:
        start, end = log.split('-')
        start, end = parse(start), parse(end)
        cnt[start] += 1
        cnt[end] -= 1
    
    for i in range(1,n):
        sumcnt[i] = cnt[i-1] + sumcnt[i-1]
    
    for i in range(1,n):
        sumarr[i] = sumarr[i-1] + sumcnt[i]
        
    temp = 0
    for i in range(adv_time, n):
        if temp < sumarr[i] - sumarr[i-adv_time]:
            ans = i-adv_time
            temp = sumarr[i] - sumarr[i-adv_time]
    
    return rparse(ans)