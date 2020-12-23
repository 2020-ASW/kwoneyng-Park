def go(m, arr, n):
    start = 0
    for i in range(len(arr)):
        cur = arr[i]
        if cur - start >= m:
            start = cur
        else:
            n -= 1
            if n < 0:
                return True
    return False

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks += [distance]
    l,r = 0, distance
    while l <= r:
        m = (l+r)//2
        if go(m, rocks, n):
            r = m - 1
        else: l = m + 1 
    return r

d,r,n = 25, [2, 14, 11, 21, 17], 2
solution(d,r,n)