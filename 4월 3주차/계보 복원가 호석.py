import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
people = input().split()
people.sort()
numbering = {}
naming = {}
for i in range(1,n+1):
    numbering[people[i-1]] = i
    naming[i-1] = people[i-1]

narr = [[] for i in range(n)]
indegree = [0]*n
m = int(input())

for _ in range(m):
    x,y = input().split()
    indegree[numbering[x]-1] += 1
    narr[numbering[y]-1].append(numbering[x]-1)

queue = deque()
for i in range(n):
    if indegree[i] == 0:
        queue.append(i)

print(len(queue))
for i in range(len(queue)):
    print(naming[queue[i]], end=' ')
print()

sons = [[] for _ in range(n)]

while queue:
    cur = queue.popleft()
    for nxt in narr[cur]:
        if indegree[nxt] == 1:
            indegree[nxt] = 0
            queue.append(nxt)
            sons[cur].append(nxt)
        elif indegree[nxt]:
            indegree[nxt] -= 1


for i in range(n):
    print(naming[i], end=' ')
    print(len(sons[i]), end=' ')
    sons[i].sort()
    for p in sons[i]:
        print(naming[p], end=' ')
    print()