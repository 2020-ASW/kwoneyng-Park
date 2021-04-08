from collections import deque
h,w,n = map(int, input().split())
paper = {}

for _ in range(n):
    r,c = map(int,input().split())
    if not paper.get(r):
        paper[r] = {}
    paper[r][c] = 1

print(paper)