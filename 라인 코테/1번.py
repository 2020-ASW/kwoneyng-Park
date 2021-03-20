def solution(table, languages, preference):
    ht = {}
    n = len(table)
    for i in range(n):
        data = table[i].split()
        company = data.pop(0)
        if not ht.get(company):
            ht[company] = {}
        for i in range(5):
            lang = data[i]
            if not ht[company].get(lang):
                ht[company][lang] = 5-i
    
    mx = 0
    ans = ''
    for company in ['SI','CONTENTS','HARDWARE','PORTAL','GAME']:
        score = 0
        for i in range(len(languages)):
            lang = languages[i]
            if ht[company].get(lang):
                score += ht[company][lang] * preference[i]
        if mx < score:
            mx = score
            ans = company
        elif mx == score:
            anss = [ans, company]
            anss.sort()
            ans = anss[0]
    
        
    return ans