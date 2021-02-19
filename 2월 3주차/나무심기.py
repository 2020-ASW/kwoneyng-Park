import sys
input = sys.stdin.readline

n = int(input())
mod = 1000000007
maxIdx = 200001
ans = 1
cnt = [0]*maxIdx
arrsum = [0]*maxIdx

treeidx = int(input()) + 1
val = treeidx
total = val
while treeidx < maxIdx:
    cnt[treeidx] += 1
    arrsum[treeidx] += val
    treeidx += treeidx&-treeidx

for i in range(1,n):
    treeidx = int(input()) + 1
    val = treeidx
    lsum = 0
    lcnt = 0

    while treeidx:
        lsum += arrsum[treeidx]
        lcnt += cnt[treeidx]
        treeidx -= treeidx&-treeidx

    ans = (ans * ((val*lcnt-lsum) + total-lsum - val*(i-lcnt)))%mod
    total += val
    treeidx = val
    while treeidx < maxIdx:
        cnt[treeidx] += 1
        arrsum[treeidx] += val
        treeidx += treeidx & -treeidx

print(ans)