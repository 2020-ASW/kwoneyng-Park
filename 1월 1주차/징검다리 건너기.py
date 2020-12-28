def go(arr, m, k):
    cnt = 1
    for i in arr:
        if i >= m:
            cnt = 1
        else:
            cnt += 1
            if cnt > k:
                return True
    return False


def solution(stones, k):
    l,r = 0, max(stones)
    while l <= r:
        m = (l+r)//2
        if go(stones, m, k):
            r = m - 1
        else:
            l = m + 1
    return r
            
        