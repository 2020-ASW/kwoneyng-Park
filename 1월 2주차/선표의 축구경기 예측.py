era = [1]*31
era[0] = 0
era[1] = 0
ft = [1,1]

for i in range(2,31):
    ft.append(ft[-1]*i)

for i in range(2,7):
    if era[i] == 1:
        mul = 2
        while i*mul < 31:
            era[i*mul] = 0
            mul += 1

for T in range(1,int(input())+1):
    a,b = map(int,input().split())
    a,b = a/100, b/100
    ana, anb = 0,0
    for i in range(31):
        if era[i] == 1:
            ta, tb = 1,1
            ta *= (ft[30] / (ft[30-i] * ft[i])) * (a**i) * ((1-a) ** (30-i))
            tb *= (ft[30] / (ft[30-i] * ft[i])) * (b**i) * ((1-b) ** (30-i))
            ana += ta
            anb += tb
    ans = 1-(1-ana)*(1-anb)
    print(f'#{T} {ans:.5f}')
    