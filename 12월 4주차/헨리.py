def calc(a,b):
    s = b//a
    while True:
        na = a*s - b
        nb = b*s
        if na < 0:
            s += 1
        elif na == 0:
            return s
        else:
            return calc(na,nb)

for T in range(int(input())):
    a,b = map(int,input().split())
    print(calc(a,b))