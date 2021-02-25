def dfs(arr,x,y,n):
    if x == n-1:
        return arr[x][y]
    left,right = dfs(arr,x+1,y,n), dfs(arr,x+1,y+1,n)
    print('x,y',x,y)
    print(left, right)
    arr[x][y] += max(left,right)
    return arr[x][y]




def solution(triangle):
    n = len(triangle)
    dfs(triangle,0,0,n)
    for i in triangle:
        print(i)

t=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(t)