class Node:
    def __init__(self, char):
        self.char = char
        self.count = 1
        self.child = {}

class Trie:
    def __init__(self):
        self.ht = {}
        self.rht = {}

    def insert(self, string, length):
        rstring = string[::-1]
        if not self.ht.get(length):
            self.ht[length] = Node(None)
            self.rht[length] = Node(None)
        head = self.ht[length]
        rhead = self.rht[length]
        head.count += 1
        rhead.count += 1
        for i in range(length):
            c = string[i]
            rc = rstring[i]

            if head.child.get(c):
                head.child[c].count += 1 # Node
            else: 
                head.child[c] = Node(c)
            if rhead.child.get(rc):
                rhead.child[rc].count += 1
            else:
                rhead.child[rc] = Node(rc)
            head = head.child[c]
            rhead = rhead.child[rc]

    def search(self,query,length):
        if self.ht.get(length):
            head = self.ht[length]
        else:
            return 0
        if not '?'*length == query:
            if query[0] == '?':
                query = query[::-1]
                head = self.rht[length]
            query = query.replace('?','')
            for i in query:
                if head.child.get(i):
                    head = head.child[i]
                else:
                    return 0
        else:
            return head.count-1
        return head.count



def solution(words, queries):
    answer = []
    trie = Trie()
    for w in words:
        trie.insert(w, len(w))

    for q in queries:
        answer.append(trie.search(q,len(q)))
    return answer