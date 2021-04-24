from math import floor
x,y = map(int,input().split())
z=floor(100*y/x)
l,r = 0, 1000000000
while l<=r :
    m = (l+r)//2
    if z == floor((y+m)*100/(x+m)):
        l = m+1
    else:
        r = m-1

if z == floor(((y+l)/(x+l))*100):
    print(-1)
else:
    print(l)