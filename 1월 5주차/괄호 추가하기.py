import sys
sys.setrecursionlimit(10000)
def perm(ls=[],st=1):
    perm_set.append(ls)
    for i in range(st,cal):
        perm(ls+[i],i+2)


n = int(input())
cal = n//2
odata = list(input())
mx = -99999999999999999999999
perm_set = []
perm()
for i in perm_set:
    data = odata[:]
    cnt = 0
    for j in range(len(i)):
        a = int(data.pop(i[j]*2-cnt*2))
        b = data.pop(i[j]*2-cnt*2)
        c = int(data.pop(i[j]*2-cnt*2))
        if b == '+':
            a += c
        elif b == '-':
            a -= c
        elif b == '*':
            a *= c
        data.insert(i[j]*2-cnt*2,a)
        cnt += 1
    while len(data) > 1:
        a = int(data.pop(0))
        b = data.pop(0)
        c = int(data.pop(0))
        if b == '+':
            a += c
        elif b == '-':
            a -= c
        elif b == '*':
            a *= c
        data.insert(0,a)
    if int(data[0]) > mx:
        mx = int(data[0])
print(mx)