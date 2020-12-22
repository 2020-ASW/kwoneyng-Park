class Node:
    def __init__(self):
        self.count = 1
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node()
        
    def insert(self,string):
        cur = self.head
        for char in string:
            if cur.child.get(char):
                cur.child[char].count += 1
            else:
                cur.child[char] = Node()
            cur = cur.child[char]
    
    def find(self,string):
        cur = self.head
        answer = 0
        for char in string:
            answer += 1
            if cur.child[char].count == 1:
                return answer
            cur = cur.child[char]
        return answer
            
def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)
    for word in words:
        answer += trie.find(word)
    return answer