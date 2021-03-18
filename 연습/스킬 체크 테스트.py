def solution(gems):
    n = len(gems)
    length = 1e9
    gemdict = {}
    l = 0
    gemset = set()
    for gem in gems:
        gemset.add(gem)
    m = len(gemset)
    ans = [1,n]
    
    for r in range(n):
        if not gemdict.get(gems[r]):
            gemdict[gems[r]] = 1
        else:
            gemdict[gems[r]] += 1
        
        if len(gemdict) == m:
            while l <= r:
                if gemdict[gems[l]] > 1:
                    gemdict[gems[l]] -= 1
                    l += 1
                else:
                    dist = r-l
                    if dist < length:
                        length = dist
                        ans = [l+1, r+1]
                    break
    
    return ans

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))