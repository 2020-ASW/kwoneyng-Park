def solution(inputString):
    n = len(inputString)
    stack = []
    ans = 0
    cnt = 0
    ht = {}
    ht['('] = 1
    ht['{'] = 2
    ht['['] = 3
    ht['<'] = 4
    rht = {}
    rht[')'] = 1
    rht['}'] = 2
    rht[']'] = 3
    rht['>'] = 4
    
    for i in range(n):
        c = inputString[i]
        if ht.get(c):
            cnt += 1
            stack.append(c)
        elif rht.get(c):
            if stack:
                if ht[stack[-1]] == rht[c]:
                    stack.pop()
                else:
                    return -i
            else:
                return -i
    
    if stack:
        return -i
        
    return cnt

inputString = 'line [({<plus>})'
print(solution(inputString))