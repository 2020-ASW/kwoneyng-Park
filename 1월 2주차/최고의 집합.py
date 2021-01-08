def solution(n, s):
    if s < n:
        return [-1]
    else:
        start = s//n
        arr = [start]*n
        dt = s - start*n
        for i in range(n-1,n-dt-1,-1):
            arr[i] += 1
        return arr