h = [4,2,0,3,2,5]
n = len(h)
eh = list(enumerate(h))
eh.sort(key=lambda x: x[1], reverse=True)
ans = 0

for i in range(n-1):
    left=eh[i]
    right=eh[i+1]
    if left[0] > right[0]:
        left,right = right,left
    mh = min(right[1],left[1])
    cnt = (right[0] - left[0] - 1)*mh
    for i in range(left[0]+1, right[0]):
        if mh < h[i]:
            cnt -= mh
        else:
            cnt -= h[i]
        h[i] = max(mh,h[i])
    ans += cnt

print(ans)