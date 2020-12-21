def calc(idx, tcal, tscr):
    global ans
    if n == idx:
        ans = max(ans, tscr)
        return
    if sum(score[idx:]) + tscr < ans:
        return
    if tcal + cal[idx] < l:
        calc(idx+1, tcal+cal[idx], tscr+score[idx])
    calc(idx+1, tcal, tscr)
    

for T in range(1,int(input())+1):
    ans = 0
    n, l = map(int,input().split())
    score = []
    cal = []
    for _ in range(n):
        s,c = map(int,input().split())
        score.append(s)
        cal.append(c)
    calc(0,0,0)


    print(f'#{T} {ans}')

    
