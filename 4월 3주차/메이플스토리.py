n, t = map(int,input().split())
idxs = [0]*1000001
exps = [0]*1000001
idx_exp = [0]*n

for idx in range(n):
    need, exp = map(int,input().split())
    idx_exp[idx] = exp
    if exps[need] < exp:
        exps[need] = exp
        idxs[need] = idx

for i in range(1,1000001):
    if exps[i-1] > exps[i]:
        idxs[i] = idxs[i-1]
        exps[i] = exps[i-1]

arr = [list(map(int,input().split())) for _ in range(n)]

for k in range(n):
    for x in range(n):
        for y in range(n):
            if x!=y and arr[x][y] < arr[x][k] + arr[k][y]:
                arr[x][y] = arr[x][k] + arr[k][y]

cur_exp = 0
cur_idx = idxs[0]
while t:
    if cur_exp < 1000001:
        nxt_idx = idxs[cur_exp]
        if idx_exp[cur_idx]*t < idx_exp[nxt_idx]*(t-arr[cur_idx][nxt_idx]):
            t -= arr[cur_idx][nxt_idx]
            cur_idx = nxt_idx
        cur_exp += idx_exp[cur_idx]
        t -= 1
    else:
        cur_exp += idx_exp[cur_idx]
        t -= 1

print(cur_exp)
