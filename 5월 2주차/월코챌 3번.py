from collections import deque

def solution(s):
    answer = []
    for item in s:
        stack = []
        pre = []
        ans = []
        for char in item:
            if char == '0' and len(stack) >= 2 and stack[-1] == stack[-2] and stack[-1] == '1':
                stack.pop()
                stack.pop()
                pre.append('110')
            else:
                stack.append(char)
        
        queue = deque(stack)
        flag = False
        while queue:
            char = queue.popleft()
            if ans[-1] == '1' and char == '1':
                ans.pop()
                for i in pre:
                    ans.append(i)
                ans.append('1')
                ans.append('1')
                flag = True
                break
            else:
                ans.append(char)
                
        if not flag:
            if ans[-1] == '1':
                ans.pop()
                for i in pre:
                    ans.append(i)
                ans.append('1')
        while queue:
            char = queue.popleft()
            ans.append(char)
        answer.append(''.join(ans))
                
        
    return answer

s = ["1110","100111100","0111111010"]
print(solution(s))