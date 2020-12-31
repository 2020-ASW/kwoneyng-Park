from collections import deque
dx,dy = [-1,0,1,0], [0,1,0,-1]

for T in range(1,int(input())+1):
    n,m,k = map(int,input().split())
    ht = {}
    vis = {}
    decrease = [0]*(k+100)
    spread = [[] for i in range(k+100)]
    q = deque()
    
    ans = 0
    for i in range(n):
        data = list(map(int,input().split()))
        for j in range(m):
            if data[j] > 0:
                q.append([i+151,j+151,data[j]])
                ans += 1

    for t in range(k+1):
        add = []
        ans -= decrease[t]
        for _ in range(len(q)):
            x,y,g = q.popleft()
            ht[(x,y)] = g
            vis[(x,y)] = 1
            if [x,y] not in spread[t+g]:
                spread[t+g+1].append([x,y])
            decrease[t+g*2] += 1

        for i,j in spread[t]:
            for p in range(4):
                xi,yi = i+dx[p], j+dy[p]
                if vis.get((xi,yi)):
                    continue
                if (xi,yi) not in add:
                    add.append((xi,yi))
                if ht.get((xi,yi)):
                    ht[(xi,yi)] = max(ht[(xi,yi)], ht[(i,j)])
                else:
                    ht[(xi,yi)] = ht[(i,j)]

        for x,y in add:
            q.append([x,y,ht[(x,y)]])
            vis[(x,y)] = 1
            ans += 1

    print(f'#{T} {ans}')
