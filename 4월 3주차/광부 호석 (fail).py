import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n, c = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

row = sorted(arr,key=lambda x:x[0])
col = sorted(arr,key=lambda x:x[1])

rht = {}
cht = {}
cnt = n
total = 0
for x,y,val in row:
    total += val
    if not rht.get(x):
        rht[x] = 0
    if not cht.get(y):
        cht[y] = 0
    rht[x] += val
    cht[y] += val

x = row[-1][0]
y = col[-1][1]
rhis = []
chis = []
while cnt > c:
    while row[-1][1] > y:
        row.pop()
    while col[-1][0] > x:
        col.pop()
    if rht[x] > cht[y]:
        # col 줄여야함
        ccnt = 0
        cval = 0
        while col[-1][1] >= y:
            tx,ty,tval = col.pop()
            if tx > x:
                continue
            rht[tx] -= tval
            total -= tval
            ccnt += 1
            cval += tval
            cnt -= 1
        chis.append([y,ccnt,cval])

        if col:
            y = col[-1][1]
    else:
        rcnt = 0
        rval = 0
        while row[-1][0] >= x:
            tx,ty,tval = row.pop()
            if ty > y:
                continue
            cht[ty] -= tval
            total -= tval
            rcnt += 1
            rval += tval
            cnt -= 1
        rhis.append([x,rcnt,rval])
        if row:
            x = row[-1][0]

while cnt < c:
    if chis and rhis:
        if chis[-1][1] + cnt <= c:
            cnt += chis[-1][1]
            total += chis[-1][2]
            chis.pop()
        elif rhis[-1][1] + cnt <= c:
            cnt += rhis[-1][1]
            total += rhis[-1][2]
            rhis.pop()
        else:
            break

print(total)
