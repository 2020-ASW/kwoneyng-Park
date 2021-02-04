from math import sqrt

for T in range(1,int(input())+1):
    p,q,r = map(int,input().split())
    a,b,c,d = map(int,input().split())

    cirXB = p-r
    cirXT = p+r
    cirYL = q-r
    cirYR = q+r
    ans = f'#{T} '
    # 빨간색이 보이기 위해?
    if cirXB < a or cirXT > c or cirYL < b or cirYR > d:
        ans += 'Y'
    else:
        ans += 'N'

    # 파란색이 보이기 위해?
    if (a-p)**2 + (b-q)**2 > r**2 or (a-p)**2 + (d-q)**2 > r**2 or (c-p)**2 + (b-q)**2 > r**2 or (c-p)**2 + (d-q)**2 > r**2:
        ans += 'Y'
    else:
        ans +='N'
    
    print(ans)