from math import log2
def make_tree(cur, parent):
    depth[cur] = depth[parent] + 1
    dp[cur][0] = parent
    max_level = int(log2(v+1))+1
    for i in range(1,max_level):
        upper = dp[cur][i-1]
        dp[cur][i] = dp[upper][i-1]
    
    for i in narr[cur]:
        cnt[cur] += make_tree(i,cur)

    return cnt[cur]

def find(a,b):
    if depth[a] < depth[b]:
        a,b = b,a

    max_depth = int(log2(v+1))+1
    if depth[a] != depth[b]:
        for i in range(int(log2(depth[a]))+2):
            if depth[dp[a][i]] < depth[b]:
                a = dp[a][i-1]
                return find(a,b)
            elif depth[dp[a][i]] == depth[b]:
                a = dp[a][i]
                break
    
    if a == b:
        return a
    while True:
        for i in range(max_depth):
            if dp[a][i] == dp[b][i]:
                if i == 0:
                    return dp[a][i]
                else:
                    a = dp[a][i-1]
                    b = dp[b][i-1]
                    break
    


for T in range(1,int(input())+1):
    v,e,a,b = map(int,input().split())
    narr = [[] for i in range(v+1)]
    data = list(map(int,input().split()))
    find_root = [0]*(v+1)
    find_root[0] = 1
    for i in range(e):
        start, end = data[i*2], data[i*2+1]
        find_root[end] += 1
        narr[start].append(end)
    
    cnt = [1]*(v+1)
    depth = [0]*(v+1)
    dp = [[0]*int(log2(v+1)+1) for _ in range(v+1)]
    depth[0] = -1
    make_tree(find_root.index(0),0)
    rs = find(a,b)
    if rs == 0:
        rs = 1
    print(f'#{T} {rs} {cnt[rs]}')