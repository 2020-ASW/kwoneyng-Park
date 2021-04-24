def whoIsMin():
    idx = 0
    val = 1e9
    rItem = 0
    for key in rdict:
        if val > rdict[key][0]:
            val = rdict[key][0]
            idx = rdict[key][1]
            rItem = key
        elif val == rdict[key][0]:
            if idx > rdict[key][1]:
                rItem = key
                idx = rdict[key][1]
    return rItem


n = int(input())
m = int(input())
arr = list(map(int,input().split()))
rdict = {}

for idx,val in enumerate(arr):
    if not rdict.get(val):
        if len(rdict) < n:
            rdict[val] = [0]*2
            rdict[val][0] = 1
            rdict[val][1] = idx
        else:
            del rdict[whoIsMin()]
            rdict[val] = [0]*2
            rdict[val][0] = 1
            rdict[val][1] = idx
    else:
        rdict[val][0] += 1

for i in sorted(list(rdict.keys())):
    print(i, end=' ')
