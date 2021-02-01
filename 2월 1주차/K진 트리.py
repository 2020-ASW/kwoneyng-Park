import sys
input = sys.stdin.readline

def where(x):
    if x == 1:
        return 0,0
    for i in range(len(depthCut)):
        if depthCut[i] >= x:
            return [i, x - depthCut[i-1] - 1]

n,k,q = map(int,input().split())
if k > 1:
    depthCut = [1]

    while depthCut[-1] + k**(len(depthCut)) < n:
        depthCut.append(depthCut[-1] + k**(len(depthCut)))

    depthCut.append(n)
    for _ in range(q):
        ans = 0
        a,b = map(int,input().split())
        depA, idxA = where(a)
        depB, idxB = where(b)
        if depA > depB:
            while depA > depB:
                ans += 1
                depA -= 1
                idxA //= k
        elif depB > depA:
            while depB > depA:
                ans += 1
                depB -= 1
                idxB //= k
        while idxA != idxB:
            ans += 2
            idxA //= k
            idxB //= k
        print(ans)


else:
    for _ in range(q):
        a,b = map(int,input().split())
        print(abs(a-b))