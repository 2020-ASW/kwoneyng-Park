from collections import deque

def dijk(s,e,w):
    q = deque()
    q.append(s)
    vis = [0]*(n+1)
    vis[s] = 1
    while q:
        cur = q.popleft() 
        for weight, nxt in narr[cur]:
            if weight >= w:
                if nxt == e:
                    return True
                if vis[nxt] == 0:
                    vis[nxt] = 1
                    q.append(nxt)
    return False

n,m = map(int,input().split())
mx = 0
mn = 999999999999
narr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    narr[a].append([c,b])
    narr[b].append([c,a])
    mx = max(mx,c)
    mn = min(mn,c)
s,e = map(int,input().split())

l,r = mn,mx

while l<=r:
    mid = (l+r)//2
    if dijk(s,e,mid):
        l = mid + 1
    else:
        r = mid -1
    
print(r)