from collections import deque

for T in range(1, 11):
    v,e = map(int,input().split())
    indgr = [0]*(v+1)
    nxt = [[] for _ in range(v+1)]
    data = list(map(int,input().split()))
    while data:
        pre = data.pop(0)
        post = data.pop(0)
        nxt[pre].append(post)
        indgr[post] += 1
    q = deque()
    for i,v in enumerate(indgr):
        if v == 0 and i:
            q.append(i)
    ans = []
    while q:
        cur = q.popleft()
        ans.append(str(cur))
        for i in nxt[cur]:
            indgr[i] -= 1
            if indgr[i] == 0:
                q.append(i)
    ans = ' '.join(ans)
    print(f"#{T} {ans}")
