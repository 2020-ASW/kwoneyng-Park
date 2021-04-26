word1,word2 = 'horse', 'ros'
n,m = len(word1), len(word2)
check = 0
for k in range(n):
    for i in range(n):
        char = word1[i]
        mn = 1e9
        idx = n
        for j in range(check,m):
            if word2[j] == char:
                if mn > j-check:
                    mn = j - check
                    idx = j
        if mn == 1e9: