def binarySearch(target):
    flag = 0
    if target % 2 == 0:
        l,r = 2,100
        time = 0
    else:
        l,r = 1,99
        flag = 1
        time = 1
    while l<=r:
        time += 1
        m = (l+r)//2
        if flag:
            if m % 2 == 0:
                m -= 1
        else:
            if m % 2 == 1:
                m -= 1
        if m == target:
            return time
        elif m > target:
            r = m - 2 
        else:
            l = m + 2


while True:
    target = int(input())
    if target == 0:
        break
    print(binarySearch(target))
    