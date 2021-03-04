def divid(n,r,c,start=0):
    if n == 1:
        return start
    if n//2 > r and n//2 > c:
        return divid(n//2,r,c,start)
    elif n//2 <= c and n//2 > r:
        return divid(n//2,r,c-n//2,start+(n//2)**2)
    elif n//2 <= r and n//2 > c:
        return divid(n//2,r-n//2,c,start+(n//2)**2*2)
    else:
        return divid(n//2,r-n//2,c-n//2,start+(n//2)**2*3)


n, r, c = map(int,input().split())
print(divid(2**n,r,c))