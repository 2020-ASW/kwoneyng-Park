def find(star,a):
    pick = 0
    starpick = 0
    ans = 0
    for i in a:
        if starpick == pick:
            if star == i:
                starpick = 1
            else:
                pick = 1
        elif starpick:
            if i != star:
                starpick = 0
                ans += 2
        elif i == star:
            pick =0
            ans += 2
    return ans

def solution(a):
    ans1 = 0
    ans2 = 0
    n = len(a)
    cnt = [0]*500001
    if n < 2:
        return 0
    if n == 2:
        return 2
    else:
        for i in a:
            cnt[i] += 1
        star = cnt.index(max(cnt))
        cnt[star] = 0
        second = cnt.index(max(cnt))
        ans1 = find(star,a)
        ans2 = find(second,a)
        
    return max(ans1, ans2)