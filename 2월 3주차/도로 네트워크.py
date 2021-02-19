import sys
from math import log2, ceil
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def makeTree(cur,pre,val=0):
    depth[cur] = depth[pre] + 1
    lcaTree[cur][0][0] = pre
    lcaTree[cur][0][1] = min(val, lcaTree[cur][0][1])
    lcaTree[cur][0][2] = max(val, lcaTree[cur][0][2])
    
    for i in range(1,maxLevel):
        lcaTree[cur][i][0] = lcaTree[lcaTree[cur][i-1][0]][i-1][0]

    for nval, nxt in narr[cur]:
        if nxt == pre:
            continue
        makeTree(nxt,cur,nval)

def find(a,b):
    mx = 0
    mn = 1e9
    if depth[a] != depth[b]:
        for i in range(maxLevel-1,-1,-1):
            if depth[lcaTree[a][i][0]] >= depth[b]:
                mx = max(lcaTree[a][i][2], mx)
                mn = min(lcaTree[a][i][1], mn)
                a = lcaTree[a][i][0]

    if a == b:
        print(mn, mx)
        return
        
    for i in range(maxLevel-1,-1,-1):
        # if depth[lcaTree[a][i][0]] != depth[lcaTree[b][i][0]]:
        if lcaTree[a][i][0] != lcaTree[b][i][0] and lcaTree[a][i][0] != 0 and lcaTree[b][i][0] != 0:
            mx = max(lcaTree[a][i][2], lcaTree[b][i][2], mx)
            mn = min(lcaTree[a][i][1], lcaTree[b][i][1], mn)
            a = lcaTree[a][i][0]
            b = lcaTree[b][i][0]

    mx = max(mx, lcaTree[a][0][2], lcaTree[b][0][2])
    mn = min(mn, lcaTree[a][0][1], lcaTree[b][0][1])

    print(mn,mx)

n = int(input())
narr = [[] for i in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    narr[a].append([c,b])
    narr[b].append([c,a])

depth = [-1]*(n+1)
maxLevel = ceil(log2(n)) + 1

lcaTree = [[[0,1e9,-1e9] for i in range(maxLevel)] for i in range(n+1)]

makeTree(1,0)

for j in range(1,maxLevel):
    for i in range(1,n+1):
        lcaTree[i][j][1] = min(lcaTree[lcaTree[i][j-1][0]][j-1][1], lcaTree[i][j-1][1])
        lcaTree[i][j][2] = max(lcaTree[lcaTree[i][j-1][0]][j-1][2], lcaTree[i][j-1][2])

# for i in lcaTree:
#     print(i)

k = int(input())
for i in range(k):
    a,b = map(int,input().split())
    if depth[a] < depth[b]:
        find(b,a)
    else:
        find(a,b)