from collections import deque

class Node:
    def __init__(self, name=None, depth=-1):
        self.name = name
        self.depth = depth
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node()

    def install(self, items):
        items.pop(0)
        head = self.head
        for item in items:
            if not head.child.get(item):
                head.child[item] = Node(item, head.depth+1)
            head = head.child[item]

    def search(self):
        head = self.head
        stack = deque()
        stack.append(head)
        while stack:
            cur = stack.pop()
            if cur.name:
                print('--'*cur.depth + cur.name)
            narr = list(cur.child.keys())
            narr.sort(reverse=True)
            for nxt in narr:
                stack.append(cur.child[nxt])


n = int(input())
trie = Trie()
for i in range(n):
    trie.install(list(input().split()))

trie.search()