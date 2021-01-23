def calc(x,y,d):
    if 0 > x:
        return calc(abs(x),y,2)
    elif x >= r:
        return calc((r-1)*2-x, y,1)
    elif 0 > y:
        return calc(x,abs(y),3)
    elif y >= c:
        return calc(x,(c-1)*2-y,4)
    return [x,y,d]

def move():
    for i in range(1,m+1):
        if (shark.get(i)):
            cur = shark[i]
            x,y = cur.x, cur.y
            if arr[x][y] == i:
                arr[x][y] = 0
            if cur.dir == 1:
                x -= cur.spd
            elif cur.dir == 2:
                x += cur.spd
            elif cur.dir == 3:
                y += cur.spd
            elif cur.dir == 4:
                y -= cur.spd
            x,y,d = calc(x,y,cur.dir)
            cur.x = x
            cur.y = y
            cur.dir = d
            if arr[x][y] > 0:
                pre = arr[x][y]
                if pre > i:
                    arr[x][y] = i
                elif shark[pre].size > cur.size:
                    del shark[i]
                else:
                    arr[x][y] = i
                    del shark[pre]
            else:
                arr[x][y] = i

class sk:
    def __init__(self, x,y,s,d,z):
        self.x = x
        self.y = y
        self.spd = s
        self.dir = d
        self.size = z

r,c,m = map(int,input().split())
arr = [[0]*c for _ in range(r)]
shark = {}
ans = 0

for i in range(1,m+1):
    x,y,s,d,z = map(int,input().split())
    x-=1; y-=1
    arr[x][y] = i
    if d < 3:
        s %= (r-1)*2
    else:
        s %= (c-1)*2
    shark[i] = sk(x,y,s,d,z)

for i in range(c):
    # for p in arr:
    #     print(p)
    # print('')
    for j in range(r):
        if arr[j][i] > 0:
            target = arr[j][i]
            arr[j][i] = 0
            ans += shark[target].size
            # print(f'man catch shark no.{target} size = {shark[target].size} in turn {i+1}')
            del shark[target]
            break
    move()

print(ans)
