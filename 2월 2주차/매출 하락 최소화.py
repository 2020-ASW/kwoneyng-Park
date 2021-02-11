from collections import deque
import sys
sys.setrecursionlimit(300000)

def find(cur, sales, narr, dp):
    dp[cur][1] = sales[cur]
    mn = 1e9
    add = 0
    if not narr[cur]:
        dp[cur][0] = 0
        return
    for nxt in narr[cur]:
        find(nxt, sales, narr, dp)
        add += min(dp[nxt][1], dp[nxt][0])
    dp[cur][1] += add
    
    for nxt in narr[cur]:
        mn = min(mn, add-min(dp[nxt][1],dp[nxt][0])+dp[nxt][1])
    dp[cur][0] = mn    
    
    
def solution(sales, links):
    answer = 0
    n = len(sales)
    dp = [[0]*2 for i in range(n)]
    narr = [[] for _ in range(n)]
    for a,b in links:
        narr[a-1].append(b-1)
    find(0, sales, narr, dp)
    # print(dp)
    return min(dp[0][1], dp[0][0])