import sys
input = sys.stdin.readline
class Node:
    def __init__(self, char):
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def install(self, string):
        head = self.head
        for char in string:
            if not head.child.get(char):
                head.child[char] = Node(char)
            head = head.child[char]
        head.child[None] = Node(None)
        
    def calc(self, item):
        head = self.head
        head = head.child[item[0]]    
        ans = 1
        for i in range(1,len(item)):
            if len(head.child) > 1:
                ans += 1
            head = head.child[item[i]]
        return ans

while True:
    try:
        n = int(input())
        items = []
        trie = Trie()
        for _ in range(n):
            item = input().rstrip()
            items.append(item)
            trie.install(item)
        ans = 0
        for item in items:
            ans += trie.calc(item)
        print(f'{round(ans/n,2):0.2f}')


    except:
        exit()