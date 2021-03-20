def quad(arr,sx,sy,ex,ey):
    val = arr[sx][sy]
    for i in range(sx,ex):
        for j in range(sy,ey):
            if arr[i][j] != val:
                single = quad(arr,sx,sy,(sx+ex)//2,(sy+ey)//2)
                double = quad(arr,sx,(sy+ey)//2,(sx+ex)//2,ey)
                triple = quad(arr,(sx+ex)//2,sy,ex,(sy+ey)//2)
                quadra = quad(arr,(sx+ex)//2,(sy+ey)//2,ex,ey)
                return f'({single}{double}{triple}{quadra})'
    return val


n = int(input())
arr = [list(map(int,input())) for _ in range(n)]

print(quad(arr,0,0,n,n))