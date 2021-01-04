from math import sqrt


def calc(i, inp, rs = []):
    cnt = len(rs)
    if cnt == 4:
        print(rs)
        return
    nxt = inp - sosu[i]
    while i >= 0:
        if nxt >= 2*(3-cnt):
            return calc(i,nxt,rs+[i])
        i -= 1


n = 1000000
inp = int(input())
era = [1]*(n+1)
era[0] = 0
era[1] = 0
sosu = []
for i in range(2,int(sqrt(n)+1)):
    if era[i] == 1:
        cur = 2
        while i*cur <= n:
            era[i*cur] = 0
            cur += 1

for i in range(1000001):
    if era[i]:
        sosu.append(i)


for i in range(len(sosu)):
    if sosu[i] >= inp:
        start = i
        break

calc(start,inp)