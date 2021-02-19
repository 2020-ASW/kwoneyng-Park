def solution(strs):
    su = [0]*(len(strs)//2+1)
    n = len(su)
    for i in range(0,len(strs),2):
        su[i//2] = int(strs[i])
    operator = []
    for i in range(1,len(strs),2):
        operator.append(strs[i])
    
    mindp = [[1e9]*n for i in range(n)]
    maxdp = [[-1e9]*n for i in range(n)]
    for i in range(n):
        mindp[i][i] = su[i]
        maxdp[i][i] = su[i]
    
    for calc in range(1,n):
        for x in range(n-calc):
            y = x+calc
            for k in range(y):
                if operator[k] == '+':                
                    maxdp[x][y] = max(maxdp[x][k] + maxdp[k+1][y], maxdp[x][y])
                    mindp[x][y] = min(mindp[x][k] + mindp[k+1][y], mindp[x][y])
                else:
                    maxdp[x][y] = max(maxdp[x][k] - mindp[k+1][y], maxdp[x][y])
                    mindp[x][y] = min(mindp[x][k] - maxdp[k+1][y], mindp[x][y])
                    
    return maxdp[0][n-1]