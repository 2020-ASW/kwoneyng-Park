def dfs(digits,start=0,s=''):
    if start == len(digits):
        ans.append(s)
        return
    cur = digits[start]
    for i in arrs[cur]:
        dfs(digits,start+1,s+i)


digits = '235'
ans = []
arrs = [[] for _ in range(10)]

print(ord('a'))
cnt = 0
start = ord('a')
for i in range(2,10):
    if i != 7 and i != 9:
        for _ in range(3):
            arrs[i].append(chr(start))
            start += 1
    else:
        for j in range(4):
            arrs[i].append(chr(start))
            start += 1

digits = list(map(int,list(digits)))


dfs(digits)
print(ans)