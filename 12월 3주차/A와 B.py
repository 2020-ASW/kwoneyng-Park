def calc_rvs(t):
    global ans
    if len(s) > len(t):
        return
    end = t[-1]
    if t == s:
        ans = 1
        return

    if end == 'B':
        calc_rvs(t[:-1][::-1])
    else:
        calc_rvs(t[:-1])

s = input()
t = input()
ans = 0
calc_rvs(t)
print(ans)