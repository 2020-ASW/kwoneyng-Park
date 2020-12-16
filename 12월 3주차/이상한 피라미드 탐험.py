def where(x):
    cut = 0
    for i in range(1,150):
        cut += i
        if x <= cut:
            return [i, x-cut+i]

for T in range(1,int(input())+1):
    a,b = map(int,input().split())
    cut = 0
    time = 0
    if a != b:
        ax, ay = where(a)
        bx, by = where(b)
        dx = ax - bx
        dy = ay - by
        if (dx > 0 and dy < 0) or (dx < 0 and dy > 0):
            time = abs(dx-dy)
        else:
            time = max(abs(dx), abs(dy)) 


    print(f'#{T} {time}')