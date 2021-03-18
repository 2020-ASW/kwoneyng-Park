factorial = [1]*(501)

for i in range(1,501):
    factorial[i] = factorial[i-1]*i

n = int(input())
rs = str(factorial[n])
s = len(rs)-1
ans = 0
while s:
    if rs[s] == '0':
        ans += 1
        s -= 1
    else:
        print(ans)
        exit()
print(ans)