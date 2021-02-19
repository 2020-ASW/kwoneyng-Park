import sys
from math import log2,ceil
input = sys.stdin.readline
sys.setrecursionlimit(20000)

def updateTree(idx,val):
    while idx:
        idx //= 2
        cntTree[idx] += 1
        idxTree[idx] += val


def sumTree(tree,l,r,ans=0):
    if l > r:
        return ans
    if l == r:
        return tree[l] + ans
    if l % 2 == 1:
        return sumTree(tree,l+1,r,ans+tree[l])
    if r % 2 == 0:
        return sumTree(tree,l,r-1,ans+tree[r])
    return sumTree(tree,l//2,r//2,ans)


n = int(input())
maxLevel = ceil(log2(200000)) + 1
mod = 1000000007

cntTree = [0]*(2**maxLevel)
idxTree = [0]*(2**maxLevel)
cost = [0]*(n+1)
maxNum = 0
adder = 2**(maxLevel-1)

for i in range(1,n+1):
    ip = int(input())
    maxNum = max(ip,maxNum)
    cntTree[ip+2**(maxLevel-1)] = 1
    idxTree[ip+2**(maxLevel-1)] = ip
    updateTree(ip+2**(maxLevel-1),ip)
    if i > 1:
        # 나보다 작은것
        cost[i] += (ip * sumTree(cntTree,adder,ip-1+adder) - sumTree(idxTree,adder,ip-1+adder))%mod
        # 나보다 큰것
        cost[i] += (sumTree(idxTree,adder+ip+1, adder+maxNum) - ip * sumTree(cntTree,adder+ip+1,adder+maxNum))%mod

ans = 1
for i in range(2,n+1):
    ans = ((ans%mod) * (cost[i] % mod))%mod

print(ans)

