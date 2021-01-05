from math import sqrt

n = int(input())
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

for i in range(n):
    if era[i]:
        sosu.append(i)

end = len(sosu)

ans = []
if n % 2 == 1:
    n -= 5
    ans.append('2')
    ans.append('3')
else:
    n -= 4
    ans.append('2')
    ans.append('2')

for i in range(end):
    for j in range(end):
        if sosu[i] + sosu[j] == n:
            ans.append(str(sosu[i]))
            ans.append(str(sosu[j]))
            print(' '.join(ans))
            exit()
print(-1)
