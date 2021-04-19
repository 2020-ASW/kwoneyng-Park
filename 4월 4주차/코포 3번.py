n = int(input())

cnt = 1
while 1+n*cnt:
    odd = 1
    even = 2
    temp = 1+n*cnt
    arr = []
    while temp > 1:
        if temp % 2 == 0:
            while temp % even == 0 and even < 100001:
                even += 2
            if even >= 100000:
                break
            temp //= even
            arr.append(even)
        else:
            while temp % odd == 0 and odd < 100001:
                odd += 2
            if odd >= 100000:
                break
            temp //= odd
            arr.append(odd)
    if temp == 1:
