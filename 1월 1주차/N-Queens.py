class Solution:
    def __init__(self):
        self.ans = []
   
    def solveNQueens(self, n: int) -> List[List[str]]:
        def put_Queen(n,idx=0,pick=[]):
            if idx == n:
                rs = []
                for i in pick:
                    row = ['.']*n
                    row[i] = 'Q'
                    rs.append(''.join(row))
                self.ans.append(rs)
                return
            
            for i in range(n):
                if not pick:
                    put_Queen(n,idx+1,pick+[i])
                elif i not in pick:
                    p = True
                    for k,v in enumerate(pick):
                        if abs(idx-k) == abs(i-v):
                            p = False
                    if p:
                        put_Queen(n,idx+1, pick+[i])
                
                
        put_Queen(n)
        return self.ans