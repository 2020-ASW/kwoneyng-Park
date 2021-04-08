import sys
input = sys.stdin.readline()
for _ in range(int(input())):
    n = int(input())
    pdict = {}
    arr = []
    for i in range(n):
        phone = input().strip()
        arr.append(phone)
    arr.sort(key=lambda x:len(x))
    ans = 'YES'
    pre = len(arr[0])
    for phone in arr:
        for i in range(pre,len(phone)):
            if pdict.get(phone[:i]):
                ans = 'NO'
                break
        pdict[phone] = 1
    print(ans)