from collections import deque
dx,dy = [-1,0,1,0],[0,1,0,-1]
def isOk(place, people, queue):
    vis = [[[0]*(people+1) for _ in range(5)] for _ in range(5)]
    for dist,num,x,y in queue:
        vis[x][y][num] = 1
        
    while queue:
        dist, num, x, y = queue.popleft()
        for i in range(4):
            xi,yi = x+dx[i], y+dy[i]
            if 0<=xi<5 and 0<=yi<5 and vis[xi][yi][num] == 0:
                vis[xi][yi][num] = 1
                if place[xi][yi] == 'P' and dist:
                    return 0
                if place[xi][yi] == 'O' and dist:
                    queue.append((dist-1,num,xi,yi))
    return 1
                

def solution(places):
    answer = []
    for place in places:
        people = 0
        queue = deque()
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people += 1
                    queue.append((2,people,i,j))
        answer.append(isOk(place,people,queue))
        
        
    return answer

place = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(place))