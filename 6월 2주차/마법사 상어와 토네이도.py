dx,dy = [0,1,0,-1], [-1,0,1,0]
n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
sx, sy = n//2, n//2
ans = 0

def check(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False

def move(x,y,p):
    global ans
    xi,yi = x+dx[p], y+dy[p]
    temp = arr[xi][yi]
    arr[xi][yi] = arr[x][y]
    arr[x][y] = 0
    total = 0
    
    if p % 2 == 0:
        # 1%
        xi,yi = x+dx[(p+1)%4], y
        adder = temp // 100
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        xi,yi = x+dx[(p+3)%4], y
        adder = temp // 100
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        # 2%
        xi,yi = x+2*dx[(p+1)%4], y+dy[p]
        adder = temp // 50
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        xi,yi = x+2*dx[(p+3)%4], y+dy[p]
        adder = temp // 50
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        # 7%
        xi,yi = x+dx[(p+1)%4], y+dy[p]
        adder = int(temp * 0.07)
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        xi,yi = x+dx[(p+3)%4], y+dy[p]
        adder = int(temp * 0.07)
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        # 10%
        xi,yi = x+dx[(p+1)%4], y+2*dy[p]
        adder = temp // 10
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        xi,yi = x+dx[(p+3)%4], y+2*dy[p]
        adder = temp // 10
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        # 5%
        xi,yi = x, y+3*dy[p]
        adder = temp // 20
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        # a
        xi,yi = x, y+2*dy[p]
        if check(xi,yi):
            arr[xi][yi] += temp - total
        else:
            ans += temp - total

    else:
        # 1%
        xi,yi = x, y+dy[(p+1)%4]
        adder = temp // 100
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        xi,yi = x, y+dy[(p+3)%4]
        adder = temp // 100
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        # 2%
        xi,yi = x+dx[p], y+2*dy[(p+1)%4]
        adder = temp // 50
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        xi,yi = x+dx[p], y+2*dy[(p+3)%4]
        adder = temp // 50
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        # 7%
        xi,yi = x+dx[p], y+dy[(p+1)%4]
        adder = int(temp * 0.07)
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        xi,yi = x+dx[p], y+dy[(p+3)%4]
        adder = int(temp * 0.07)
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        # 10%
        xi,yi = x+2*dx[p], y+dy[(p+1)%4]
        adder = temp // 10
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        xi,yi = x+2*dx[p], y+dy[(p+3)%4]
        adder = temp // 10
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        # 5%
        xi,yi = x+3*dx[p], y
        adder = temp // 20
        total += adder
        if check(xi,yi):
            arr[xi][yi] += adder
        else:
            ans += adder

        # a
        xi,yi = x+2*dx[p], y
        if check(xi,yi):
            arr[xi][yi] += temp - total
        else:
            ans += temp - total


length = 1
p = 0
while sx > 0 or sy > 0:
    for i in range(length):
        move(sx,sy,p)
        sx+=dx[p]; sy+=dy[p]
        if sx == 0 and sy == 0:
            break
    p += 1

    if sx == 0 and sy == 0:
        break

    for i in range(length):
        move(sx,sy,p)
        sx+=dx[p]; sy+=dy[p]
    p = (p+1)%4
    length += 1

print(ans)