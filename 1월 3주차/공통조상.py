from math import log2

def makeTree(cur, parent):
    depth[cur] = depth[parent] + 1 # 자식노드 차수가 부모노드 + 1
    dp[cur][0] = parent

    for i in range(1,mxL):
        upper = dp[cur][i-1] #1 2^n
        if upper == 0:
            break
        dp[cur][i] = dp[upper][i-1]
        # dp[13][2] = dp[6][1]

    for child in narr[cur]:
        cnt[cur] += makeTree(child, cur)
    return cnt[cur]

def find(a,b):
    if depth[a] == depth[b]:
        # start
        for i in range(mxL):
            if dp[a][i] == dp[b][i]:
                if i == 0:
                    return dp[a][0]
                return find(dp[a][i-1], dp[b][i-1])
    
    if depth[a] < depth[b]:
        a,b = b,a
    
    for i in range(mxL):
        if depth[b] > depth[dp[a][i]]:
            return find(dp[a][i-1],b)


for T in range(1,int(input())+1):
    v,e,st,ed = map(int,input().split())
    data = list(map(int,input().split()))
    narr = [[] for _ in range(v+1)]
    mxL = int(log2(v))+1 # 최대 점프하는 수
    for i in range(e):
        narr[data[i*2]].append(data[i*2+1])

    depth = [0]*(v+1)
    depth[0] = -1
    dp = [[0]*mxL for _ in range(v+1)]  # dp[node][jump한 수 (2^n)]
    cnt = [1]*(v+1)
    makeTree(1,0)
    ans = find(st,ed)
    rs = cnt[ans]
    print(ans, rs)
