import sys
input = sys.stdin.readline

n,m = map(int,input().split())
numberToName = {}
nameToNumber = {}

for i in range(1,n+1):
    numberToName[i] = input().rstrip()
    nameToNumber[numberToName[i]] = i

for i in range(m):
    query = input().rstrip()
    if query.isdigit():
        print(numberToName[int(query)])
    else:
        print(nameToNumber[query])

