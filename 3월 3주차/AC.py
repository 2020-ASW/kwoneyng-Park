import sys
input = sys.stdin.readline

for T in range(int(input())):
    order = input()
    n = int(input())
    arr = input().rstrip()[1:-1].split(',')
    if n == 0:
        arr = []

    reverse = False
    l,r = 0,n
    ans = ''
    for o in order:
        if o == 'R':
            reverse = not reverse
        elif o == 'D':
            if reverse:
                r -= 1
            else:
                l += 1
    if l > r:
        print('error')
    else:
        if reverse:
            print('['+','.join(reversed(arr[l:r])) +']')
        else:
            print('[' +','.join(arr[l:r]) +']')