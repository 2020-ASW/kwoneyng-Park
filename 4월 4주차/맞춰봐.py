def search(su,rs):
    if su == len(rs):
        for i in rs:
            print(i, end=' ')
        exit()

    if arr[su][su] == '0':
        search(su+1,rs)
    for i in (range(1,11) if arr[su][su] == '+' else range(-10,0)):
        flag = True
        for j in range(su):
            calc = sum(rs[j:]) + i
            if calc < 0 and arr[j][su] != '-':
                flag = False
                break
            elif calc > 0 and arr[j][su] != '+':
                flag = False
                break
            elif calc == 0 and arr[j][su] != '0':
                flag = False
                break
        if flag:
            rs[su] = i
            search(su+1,rs)
            rs[su] = 0


n = int(input())
string = input()

arr = [['']*(n) for i in range(n)]
rs = [0]*n
cnt = 0
for i in range(n):
    for j in range(i,n):
        arr[i][j] = string[cnt]
        cnt += 1

search(0,rs)
