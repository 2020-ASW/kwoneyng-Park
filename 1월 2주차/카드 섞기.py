def check():
    for i in range(n):
        if temp[i] != p[i]:
            return False
    return True

def sf():
    ls = [0]*n
    for i in range(n):
        ls[i] = temp[s[i]]
    return ls

n = int(input())

p = list(map(int,input().split()))
s = list(map(int,input().split()))

temp = [i%3 for i in range(n)]

ans = 0
while True:
    flag = 0
    if check():
        break
    temp = sf()
    for i in range(n):
        if temp[i] != i%3:
            flag = 1
            break
    if flag == 0:
        print(-1)
        exit()
    ans += 1
print(ans)