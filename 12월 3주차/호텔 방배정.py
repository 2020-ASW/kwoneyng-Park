import sys
sys.setrecursionlimit(200000)
ht = {}
def find(x):
    if not ht.get(x):
        ht[x] = x+1
    else:
        ht[x] = find(ht[x])
        
    return ht[x]
    
def solution(k, room_number):
    answer = []
    for i in room_number:
        answer.append(find(i)-1)
    return answer