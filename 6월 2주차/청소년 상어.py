from collections import deque
near = [[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1]]

bd = [[0]*4 for i in range(4)]

fish = [0]*17
for i in range(4):
    data = list(map(int,input().split()))
    for j in range(4):
        bd[i][j] = data[j*2]
        fish[data[j*2]] = data[j*2+1]

def search(bd,i):
    for x in range(4):
        for y in range(4):
            if bd[x][y] == i:
                return x,y

def move(bd,fish):
    for i in range(1,17):
        if fish[i] == -1:
            continue
        x,y = search(bd,i)
        for p in range(8):
            nxp = (fish[i]+p)%8
            dx,dy = near[nxp]
            xi,yi = x+dx,y+dy
            if 0<=xi<4 and 0<=yi<4 and bd[xi][yi] != -1:
                bd[xi][yi],bd[x][y] = bd[x][y],bd[xi][yi]
                fish[i] = nxp
                break

dead = bd[0][0]
sk = fish[dead]
fish[dead] = -1
bd[0][0] = -1
q = deque()
ans = 0
q.append([[i[:] for i in bd], sk, fish[:], dead]) # bd, sk, fish, ans

def prt(bd):
    for i in bd:
        print(i)
    print('-------------------')

while q:
    bd,sk,fish,rs = q.pop()
    move(bd,fish)
    # prt(bd)
    x,y = search(bd,-1)
    dx,dy = near[sk]
    xi,yi = x+dx, y+dy
    while (0<=xi<4 and 0<=yi<4):
        if bd[xi][yi] > 0:
            nbd = [i[:] for i in bd]
            nbd[x][y] = 0
            dead = nbd[xi][yi]
            nsk = fish[dead]
            nfish = fish[:]
            nfish[dead] = -1
            nbd[xi][yi] = -1
            if rs+dead > ans:
                ans = rs+dead
            q.append([nbd,nsk,nfish,rs+dead])
            xi += dx
            yi += dy
        else:
            xi += dx
            yi += dy

print(ans)
                
