from math import log2
import sys
input = sys.stdin.readline

def makeTree(child, parent, cost):
    vis[child] = 1
    depth[child] = depth[parent] + 1
    if parent > 0:
        parents[child][0] = [parent,cost,cost]

    for level in range(1,maxLevel):
        pjump = parents[parents[child][level-1][0]][level-1]
        if pjump[0] == 0:
            break
        parents[child][level][0] = pjump[0]
        parents[child][level][1] = min(cost,pjump[1])
        parents[child][level][2] = max(cost,pjump[2])

    for ncost, nxt in narr[child]:
        if vis[nxt] == 0:
            makeTree(nxt, child, ncost)

def find(a,b):
    mn,mx = min(parents[a][0][1], parents[b][0][1]), max(parents[a][0][2],parents[b][0][2])

    if depth[a] < depth[b]:
        a,b = b,a
    if depth[a] != depth[b]:
        for i in range(maxLevel-1,-1,-1):
            if depth[parents[a][i][0]] >= depth[b]:
                mn = min(parents[a][i][1], mn)
                mx = min(parents[a][i][2], mx)
                a = parents[a][i][0]

    # a와 b의 depth가 같아짐
    if a != b:
        for i in range(maxLevel-1,-1,-1):
            if parents[a][i][0] != parents[b][i][0] and parents[a][i][0] != 0 and parents[b][i][0] != 0:
                mn = min(mn, parents[a][i][1], parents[b][i][1])
                mx = max(mx, parents[a][i][2], parents[b][i][2])
                a = parents[a][i][0]
                b = parents[b][i][0]
        mn = min(mn,parents[a][0][1],parents[b][0][1])
        mx = max(mx,parents[a][0][2],parents[b][0][2])

    print(mn,mx)


n = int(input())

narr = [[] for i in range(n+1)]

for i in range(n-1):
    a,b,v = map(int,input().split())
    narr[a].append([v,b])
    narr[b].append([v,a])

maxLevel = int(log2(n)) + 1
vis = [0]*(n+1)
parents = [[[0,1e9,-1e9]for i in range(maxLevel)] for i in range(n+1)]

depth = [0]*(n+1)
depth[0] = -1
makeTree(1,0,0)

# for i in parents:
#     print(i)

# print(depth)

k = int(input())
for i in range(k):
    a,b = map(int,input().split())
    find(a,b)
