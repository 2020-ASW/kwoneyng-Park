from collections import OrderedDict

def solution(n, k, cmd):
    answer = ''
    stack = []
    arr = [1]*n
    for c in cmd:
        if len(c) > 1:
            p,x = c.split()
            x = int(x)
            if p == 'U':
                while (x and k):
                    k-=1
                    if arr[k]:
                        x-=1
            else:
                while (x and k<n):
                    k+=1
                    if arr[k]:
                        x-=1
            
        elif c == 'C':
            arr[k] = 0
            stack.append(k)
            st = k
            while k < n and not arr[k]:
                k+=1
            if k == n:
                k = st-1
            
        else:
            arr[stack.pop()] = 1
            
    for i in arr:
        if i:
            answer += 'O'
        else:
            answer += 'X'
            
    return answer

n,k,cmd = 8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n,k,cmd))