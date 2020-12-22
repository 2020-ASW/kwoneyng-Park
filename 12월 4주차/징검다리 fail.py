def go(rocks, lim, n):
    mn = 999999999999
    for i in range(len(rocks)-1):
        mn = min(mn,rocks[i+1]-rocks[i])
            
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.insert(0,0)
    rocks.append(distance)
    l, r = 0, distance
    while l <= r:
        mid = (l+r)//2
        if go(rocks, mid, n):
            l = mid + 1
        else:
            r = mid - 1
    return r
        
d,r,n = 	25, [2, 14, 11, 21, 17], 2
solution(d,r,n)