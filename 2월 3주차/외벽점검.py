from itertools import permutations

def check(perm, temp):
    n = len(temp)
    idx = 0
    for run in perm:
        while True:
            n -= 1
            if n == 0:
                return True
            loc = temp[idx]
            idx += 1
            dt = temp[idx] - loc
            if run >= dt:
                run -= dt
            else:
                break
    return False
                
            
def solution(n, weak, dist):
    m = len(dist)
    dist.sort(reverse=True)
    for people in range(1,m+1):
        perms = permutations(dist,people)
        for perm in perms:
            for i in range(len(weak)):
                temp = weak[i:] + weak[:i]
                for j in range(i):
                    temp[len(weak)-i+j] += n
                if check(perm, temp):
                    return people
            
    return -1