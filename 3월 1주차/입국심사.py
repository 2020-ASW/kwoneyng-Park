def solution(n, times):
    l,r = 0, max(times)*n//len(times)
    while l < r:
        cnt = 0
        m = (l+r)//2
        for v in times:
            cnt += m//v
        if cnt < n:
            l = m+1
        else:
            r = m
    return l