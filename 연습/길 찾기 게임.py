import sys
sys.setrecursionlimit(10000)

class Node:
    def __init__(self,val,nid):
        self.nid = nid 
        self.val = val
        self.left = None
        self.right = None
        
class binaryTree:
    def __init__(self):
        self.head = None
        
    def insert(self,val,nid):
        if not self.head:
            self.head = Node(val,nid)
            return
        cur = self.head
        while True:
            if val > cur.val:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(val,nid)
                    return
            else:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(val,nid)
                    return
    
    def preorder(self):
        ans = []
        head = self.head
        stack = [head]
        while stack:
            cur = stack.pop()
            ans.append(cur.nid)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return ans
    
def postorder(cur):
    if cur.left:
        postorder(cur.left)
    if cur.right:
        postorder(cur.right)
    post.append(cur.nid)
    return post
        
        
post = []
def solution(nodeinfo):
    n = len(nodeinfo)
    for i in range(1,n+1):
        nodeinfo[i-1].append(i)
    nodeinfo.sort(key=lambda x:x[1],reverse=True)
    bt = binaryTree()
    for val,_,node in nodeinfo:
        bt.insert(val,node)
        
    return [bt.preorder(), postorder(bt.head)]