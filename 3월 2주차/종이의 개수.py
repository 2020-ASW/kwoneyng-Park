def check(arr,x,y,n):
    su = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if su != arr[i][j]:
                check(arr,x,y,n//3)
                check(arr,x,y+n//3,n//3)
                check(arr,x,y+2*n//3,n//3)
                check(arr,x+n//3,y,n//3)
                check(arr,x+n//3,y+n//3,n//3)
                check(arr,x+n//3,y+2*n//3,n//3)
                check(arr,x+2*n//3,y,n//3)
                check(arr,x+2*n//3,y+n//3,n//3)
                check(arr,x+2*n//3,y+2*n//3,n//3)
                return
    if ht.get(su):
        ht[su] += 1
    else:
        ht[su] = 1
    

n = int(input())
ht = {}
arr = [list(map(int,input().split())) for _ in range(n)]
check(arr,0,0,n)
for i in range(-1,2):
    if ht.get(i):
        print(ht[i])
    else:
        print(0)