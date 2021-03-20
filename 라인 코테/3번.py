def solution(enter, leave):
    n = len(enter)
    et = {}
    lv = {}
    ans = []
    for i in range(n):
        ep = enter[i]
        et[ep] = set(enter[i+1:])
        lp = leave[i]
        lv[lp] = set(leave[:i])
        
    rs = {}
    for i in range(1,n+1):
        if not rs.get(i):
            rs[i] = set()
        for j in et[i]&lv[i]:
            rs[i].add(j)
            if not rs.get(j):
                rs[j] = set()
            rs[i] = rs[i] | rs[j]
        for j in rs[i]:
            if not rs.get(j):
                rs[j] = set()
            rs[j].add(i)
            
    for i in range(1,n+1):
        ans.append(len(rs[i]))
    
    return ans