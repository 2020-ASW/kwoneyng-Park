from collections import deque

def check(string):
    stack = deque()
    n = len(string)
    for char in string:
        if char == '{' or char == '[' or char == '(':
            stack.append(char)
        elif char == '}' and stack[-1] == '{':
            stack.pop()
        elif char == ')' and stack[-1] == '(':
            stack.pop()
        elif char == ']' and stack[-1] == '[':
            stack.pop()
        else:
            return False
    return True

def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        ns = s[i:] + s[:i]
        if check(ns):
            answer += 1
        
        
    return answer

s = ""
print(solution(s))