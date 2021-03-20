def solution(inp_str):
    ans = []
    
    if 8<=len(inp_str)<=15:
        pass
    else:
        ans.append(1)
        
    chars = {}
    count = 1
    types = [0]*4
    pre_str = 'asd'
    for ch in inp_str:
        if ord('A') <= ord(ch) <= ord('Z'):
            tp = 0
            types[tp] = 1
        elif ord('a') <= ord(ch) <= ord('z'):
            tp = 1
            types[tp] = 1
        elif ord('0') <= ord(ch) <= ord('9'):
            tp = 2
            types[tp] = 1
        elif ch in ['~','!','@','#','$','%','^','&','*']:
            tp = 3
            types[tp] = 1
        elif 2 not in ans:
            ans.append(2)
        if pre_str == ch:
            count += 1
            if count >= 4:
                if not 4 in ans:
                    ans.append(4)
        else:
            count = 1
            pre_str = ch
        if not chars.get(ch):
            chars[ch] = 0
        chars[ch] += 1
        if chars[ch] >= 5:
            if not 5 in ans:
                ans.append(5)
    if sum(types) < 3:
        ans.append(3)
    
    ans.sort()
    if ans:
        return ans
    else:
        return [0]
        