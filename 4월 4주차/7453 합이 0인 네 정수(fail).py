import sys
input = sys.stdin.readline
n = int(input())

A,B,C,D = [],[],[],[]
for i in range(n):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
AB = {}

for i in range(n):
    for j in range(n):
        ab = A[i] + B[j]
        AB[ab] = AB.get(ab,0) + 1
       

ans = 0
for i in range(n):
    for j in range(n):
        cd = C[i] + D[j]
        if AB.get(-cd):
            ans += AB.get(-cd)

print(ans)

# 
