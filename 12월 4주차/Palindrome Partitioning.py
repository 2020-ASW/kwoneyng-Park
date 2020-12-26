def palindrome(idx=0,li=[]):
    if idx >= n:
        ans.append(li)
        return
    palindrome(idx+1,li+[s[idx]])
    if idx < n and li and li[-1] == s[idx]:
        rf = li.pop()
        palindrome(idx+1,li+[s[idx]*2])
        li.append(rf)

    if li:    
        ns = li.pop()
        if idx < n and li:
            if li[-1] == s[idx]:
                ns = li.pop() + ns + s[idx]
                palindrome(idx+1,li+[ns])

s = 'aabaa'
n = len(s)
ans = []
palindrome()
print(ans)