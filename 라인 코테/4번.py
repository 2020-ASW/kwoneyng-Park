class Node:
    def __init__(self,nid=0,val=None,pid=None):
        self.nid = nid
        self.val = val
        self.pid = pid
        
def search(leaf,word):
    n = len(word)
    item = leaf[0]
    m = len(item)
    nid = leaf[1]
    l = 0
    cnt = 0
    start = []
    while l <= m-n:
        if item[l] == word[0]:
            if item[l:l+n] == word:
                cnt = 0
                start.append(l)
                l += n
        else:
            l += 1
    if cnt == 0:
        return False
    return [cnt, start, item]
        
    
    
    

def solution(data, word):
    answer = []
    n = len(data)
    indegree = [0]*(n+1)
    nodes = [0]*(n+1)
    nodes[0] = Node()
    valNodes = {}
    leafs = []
    for detail in data:
        nid, val, pid = detail.split()
        nid = int(nid)
        pid = int(pid)
        nodes[nid] = Node(nid,val,pid)
        indegree[pid] += 1
        
    for i in range(1,n+1):
        if not indegree[i]:
            valNodes[nodes[i].val] = i
            leafs.append([nodes[i].val,i])
    
    firstID = 0
    rs = []
    for leaf in leafs:
        if leaf[0] == word:
            firstID = [leaf[1]]
        check = search(leaf,word)
        if check:
            rs.append(check)
    
    print(rs)
    return answer

data = ["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"]
word = "BROWN"

solution(data, word)