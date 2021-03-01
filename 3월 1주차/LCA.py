import sys
from math import log2,ceil
input = sys.stdin.readline
sys.setrecursionlimit(50001)

def makeTree(child, parent):
    if depth[child] != -1:
        return
    depth[child] = depth[parent]+1
    LCATree[child][0] = parent
    for jump in range(1,maxLevel):
        LCATree[child][jump] = LCATree[LCATree[child][jump-1]][jump-1]
    for nxt in narr[child]:
        makeTree(nxt, child)

def find(a,b):
    if depth[a] != depth[b]:
        for i in range(maxLevel-1,-1,-1):
            if depth[LCATree[a][i]] >= depth[b]:
                a = LCATree[a][i]
    
    if a == b:
        return a

    for i in range(maxLevel-1,-1,-1):
        if LCATree[a][i] and LCATree[b][i] and LCATree[a][i] != LCATree[b][i]:
            a = LCATree[a][i]
            b = LCATree[b][i]
    
    return LCATree[a][0]


n = int(input())
narr = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    narr[a].append(b)
    narr[b].append(a)
depth = [-1]*(n+1)
maxLevel = ceil(log2(n))+1

LCATree = [[0]*maxLevel for _ in range(n+1)]
makeTree(1,0)
m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    if depth[a] < depth[b]:
        print(find(b,a))
    else:
        print(find(a,b))
