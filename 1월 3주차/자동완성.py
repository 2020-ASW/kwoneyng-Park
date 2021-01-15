class Node:
    def __init__(self):
        self.cnt = 1
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node()

    def ready(self,word):
        head = self.head
        for w in word:
            if not head.child.get(w):
                head.child[w] = Node()
            else:
                head.child[w].cnt += 1
            head = head.child[w]
    
    def find(self,word):
        head = self.head
        ans = 0
        for w in word:
            ans += 1
            head = head.child[w]
            if head.cnt == 1:
                return ans
        return ans

words = ['go','gone','guild']
trie = Trie()
for word in words:
    trie.ready(word)

ans = 0
for word in words:
    ans += trie.find(word)

print(ans)