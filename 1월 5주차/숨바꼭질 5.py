from collections import deque

def go(root):
    global k
    q = deque([n])
    cnt = 0
    while q:
        # 탈출조건
        if root[cnt%2][k] >= 0:
            print(cnt)
            return

        # 시간 마다 움직임
        cnt += 1
        for i in range(len(q)):
            cur = q.popleft()
            if cur-1 >= 0:
                if root[cnt%2][cur-1] < 0:
                    q.append(cur-1)
                    root[cnt%2][cur-1] = cnt 
            if cur+1 < 500001:
                if root[cnt%2][cur+1] < 0:
                    q.append(cur+1)
                    root[cnt%2][cur+1] = cnt
            if cur*2 < 500001:
                if root[cnt%2][cur*2] < 0:
                    root[cnt%2][cur*2] = cnt
                    q.append(cur*2)
        k += cnt
        if k > 500000:
            print(-1)
            return

n,k = map(int,input().split())
root = [[-1]*500001 for i in range(2)]
root[0][n] = 0
go(root)